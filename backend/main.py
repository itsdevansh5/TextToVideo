
from fastapi import FastAPI, HTTPException
from schemas import VideoRequest, VideoResponse
from agent.prompt_enhancer import enhance_prompt
from agent.style_mapper import apply_style
from services.video_generator import generate_video

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Prompt2Video AI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate", response_model=VideoResponse)
def generate_video_endpoint(request: VideoRequest):
    try:
        enhanced = enhance_prompt(request.prompt)
        styled_prompt = apply_style(enhanced, request.style)
        video_url = generate_video(styled_prompt)

        return VideoResponse(
            enhanced_prompt=styled_prompt,
            video_url=video_url
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
