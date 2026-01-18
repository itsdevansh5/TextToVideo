# Prompt2Video 🎬

Prompt2Video is an AI-powered web application that converts natural
language text prompts into short videos using a modular, agent-based
backend pipeline and modern generative AI models.

The project demonstrates real-world AI system design, API integration,
and deployment practices by combining prompt processing, style control,
and video generation into a clean, user-facing web demo.

------------------------------------------------------------------------

## Deployment

-  ** Web App link - 
https://texttovideobydevansh.netlify.app/


------------------------------------------------------------------------
## 🚀 Features

-   **Text-to-Video Generation**
-   **Prompt Enhancement Module (LLM-pluggable)**
-   **Style Selection (Cinematic, Animation, Realistic)**
-   **Deployed Web Demo**
-   **Production-Oriented API Design**

------------------------------------------------------------------------

## 🧠 System Architecture

1.  User submits a text prompt and selects a style
2.  Prompt enhancement module enriches the input
3.  Style mapper injects visual parameters
4.  Video generation via Replicate-hosted model
5.  Backend polls inference status
6.  Video URL returned to frontend

------------------------------------------------------------------------

## 🛠 Tech Stack

### Backend

-   Python
-   FastAPI
-   Replicate API

### Frontend

-   HTML
-   CSS
-   JavaScript

### AI

-   Text-to-video generation models
-   Modular prompt enhancement pipeline

------------------------------------------------------------------------

## ⚙️ Setup & Installation

### Backend

``` bash
pip install -r requirements.txt
uvicorn main:app
```

Create `.env` file:

``` env
REPLICATE_API_TOKEN=your_token_here
```

### Frontend

Open `index.html` or deploy via Netlify/Vercel.

------------------------------------------------------------------------

## 🎥 Usage

1.  Enter prompt
2.  Select style
3.  Generate video
4.  View result

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Scene segmentation
-   Async job queues
-   Audio generation
-   Advanced camera control

------------------------------------------------------------------------

## 👨‍💻 Author

Devansh Trivedi
