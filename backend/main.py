
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading, uuid, hashlib, time

from schemas import VideoRequest
from store import jobs
from cache import cache
from services.video_generator import generate_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
def generate(request: VideoRequest):
    key = hashlib.md5(
        f"{request.prompt}_{request.style}".encode()
    ).hexdigest()

    if key in cache:
        return {
            "cached": True,
            "video_url": cache[key]
        }

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "pending",
        "message": "Job created",
        "video_url": None,
        "error": None
    }

    def run():
        try:
            jobs[job_id]["status"] = "running"
            jobs[job_id]["message"] = "Enhancing prompt"
            time.sleep(1)

            jobs[job_id]["message"] = "Generating video (this may take some time)"
            video_url = generate_video(request.prompt)

            jobs[job_id]["message"] = "Finalizing"
            jobs[job_id]["status"] = "done"
            jobs[job_id]["video_url"] = video_url
            cache[key] = video_url

        except Exception as e:
            jobs[job_id]["status"] = "failed"
            jobs[job_id]["error"] = str(e)
            jobs[job_id]["message"] = "Failed"

    threading.Thread(target=run).start()

    return {
        "cached": False,
        "job_id": job_id
    }

@app.get("/status/{job_id}")
def status(job_id: str):
    return jobs.get(job_id, {"error": "Invalid job id"})
