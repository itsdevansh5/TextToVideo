
import requests
import time
from config import REPLICATE_API_TOKEN

REPLICATE_URL = "https://api.replicate.com/v1/predictions"

HEADERS = {
    "Authorization": f"Token {REPLICATE_API_TOKEN}",
    "Content-Type": "application/json"
}

MODEL_VERSION = "minimax/video-01"

def generate_video(prompt: str) -> str:
    payload = {
        "version": MODEL_VERSION,
        "input": {
            "prompt": prompt,
            "duration": 3,
            "fps": 8
        }
    }

    res = requests.post(REPLICATE_URL, json=payload, headers=HEADERS)
    res.raise_for_status()

    prediction_id = res.json()["id"]
    status_url = f"{REPLICATE_URL}/{prediction_id}"

    while True:
        status = requests.get(status_url, headers=HEADERS).json()

        if status["status"] == "succeeded":
            output = status["output"]
            return output[0] if isinstance(output, list) else output

        if status["status"] == "failed":
            raise Exception("Video generation failed")

        time.sleep(5)
