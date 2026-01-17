
import requests
import time
from config import HF_API_TOKEN

HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"
HF_API_URL = f"https://router.huggingface.co/hf-inference/models/{HF_MODEL}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def _fallback(prompt: str) -> str:
    """Deterministic fallback to guarantee demo stability"""
    return (
        f"{prompt}, highly detailed, cinematic lighting, smooth camera motion, "
        "shallow depth of field, ultra realistic, professional film look, 4k quality"
    )

def enhance_prompt(prompt: str) -> str:
    payload = {
        "inputs": (
            "You are an expert prompt engineer for text-to-video generation. "
            "Rewrite the user prompt by adding cinematic visuals, camera movement, "
            "lighting, realism. Keep it concise.\n\n"
            f"User prompt: {prompt}\n\nEnhanced prompt:"
        ),
        "parameters": {
            "max_new_tokens": 120,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    for attempt in range(2):  # retry once
        try:
            response = requests.post(
                HF_API_URL,
                headers=HEADERS,
                json=payload,
                timeout=30
            )

            # Common HF router failures
            if response.status_code in (403, 404, 410, 429, 503):
                time.sleep(3)
                continue

            response.raise_for_status()
            data = response.json()

            return data[0]["generated_text"].strip()

        except Exception:
            time.sleep(2)

    # FINAL SAFETY NET
    return _fallback(prompt)
