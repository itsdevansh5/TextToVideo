
from pydantic import BaseModel

class VideoRequest(BaseModel):
    prompt: str
    style: str

class VideoResponse(BaseModel):
    enhanced_prompt: str
    video_url: str
