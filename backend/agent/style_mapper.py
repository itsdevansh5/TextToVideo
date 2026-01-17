
def apply_style(prompt: str, style: str) -> str:
    style = style.lower()

    if style == "cinematic":
        return f"{prompt}, cinematic lighting, shallow depth of field, dramatic camera movement, ultra realistic"

    if style == "animation":
        return f"{prompt}, animated style, vibrant colors, smooth motion, stylized characters"

    if style == "realistic":
        return f"{prompt}, photorealistic, natural lighting, real-world physics, high detail"

    return prompt
