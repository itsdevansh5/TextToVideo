
import requests
from config import REPLICATE_API_TOKEN

REPLICATE_URL = "https://api.replicate.com/v1/predictions"

HEADERS = {
    "Authorization": f"Token {REPLICATE_API_TOKEN}",
    "Content-Type": "application/json"
}

# ✅ FREE TEXT-TO-VIDEO MODEL
MODEL_VERSION = "minimax/video-01"

def generate_video(prompt: str) -> str:
    payload = {
        "version": MODEL_VERSION,
        "input": {
            "prompt": prompt,
            "duration": 4,      # seconds
            "fps": 12
        }
    }

    response = requests.post(REPLICATE_URL, json=payload, headers=HEADERS)
    response.raise_for_status()

    prediction = response.json()
    prediction_id = prediction["id"]

    status_url = f"{REPLICATE_URL}/{prediction_id}"

    while True:
        result = requests.get(status_url, headers=HEADERS).json()

        if result["status"] == "succeeded":
            output = result["output"]
            return output[0] if isinstance(output, list) else output

        if result["status"] == "failed":
            raise Exception("Video generation failed")
