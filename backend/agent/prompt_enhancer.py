
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def enhance_prompt(prompt: str) -> str:
    system_prompt = f"""
    You are an AI prompt engineer for text-to-video generation.

    Improve the following prompt by adding:
    - visual details
    - camera motion
    - lighting
    - realism
    - cinematic quality

    Keep it concise and descriptive.

    Prompt: {prompt}
    """

    response = model.generate_content(system_prompt)
    return response.text.strip()
