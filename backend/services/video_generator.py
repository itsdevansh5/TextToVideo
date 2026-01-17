
import requests
from config import REPLICATE_API_TOKEN

REPLICATE_URL = "https://api.replicate.com/v1/predictions"

HEADERS = {
    "Authorization": f"Token {REPLICATE_API_TOKEN}",
    "Content-Type": "application/json"
}

MODEL_VERSION = "anotherjesse/zeroscope-v2-xl"  # text-to-video

def generate_video(prompt: str) -> str:
    payload = {
        "version": MODEL_VERSION,
        "input": {
            "prompt": prompt,
            "num_frames": 24,
            "fps": 8
        }
    }

    response = requests.post(REPLICATE_URL, json=payload, headers=HEADERS)
    response.raise_for_status()

    prediction = response.json()

    # Polling (simple version)
    prediction_id = prediction["id"]
    status_url = f"{REPLICATE_URL}/{prediction_id}"

    while True:
        result = requests.get(status_url, headers=HEADERS).json()
        if result["status"] == "succeeded":
            return result["output"]
        if result["status"] == "failed":
            raise Exception("Video generation failed")
