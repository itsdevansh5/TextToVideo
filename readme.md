# Prompt2Video 🎬  
**An Asynchronous AI Text-to-Video Generation System with Live Progress Tracking**

🌐 **Live Demo:** https://texttovideobydevansh.netlify.app/

---

## 📌 Overview

Prompt2Video is a full-stack AI application that converts natural language prompts into short videos using modern generative AI models.

The project focuses on real-world AI system design challenges such as long-running inference, non-blocking APIs, asynchronous execution, and user experience during slow operations.

---

## 🚀 Key Features

- Text-to-video generation  
- Asynchronous backend architecture  
- Live progress updates via status polling  
- Job-based execution model  
- Prompt enhancement pipeline  
- Style selection  
- Deployed web application  

---

## 🏗 System Architecture

Frontend → FastAPI Backend → Background Worker → AI Video Model

The frontend polls the backend for live job updates while video generation runs asynchronously.

---

## 🔁 Asynchronous Job Model

Video generation is GPU-intensive and slow.  
The backend avoids blocking requests by creating a job, returning immediately, and processing the task in a background thread.

---

## 🧩 Job Lifecycle

Each job stores:
- status
- message
- video_url
- error

Live messages represent real backend execution stages.

---

## 🔄 Live Status Polling

The frontend periodically requests job status using:

GET /status/{job_id}

This keeps the UI responsive and transparent.

---

## 🧵 Background Execution

Python multithreading allows heavy AI inference to run without blocking HTTP requests.

---

## ⚡ Performance Considerations

- Reduced video duration and FPS
- Polling-based progress updates
- Focus on perceived performance

---

## 🛠 Tech Stack

Backend:
- Python
- FastAPI
- Multithreading
- Replicate API

Frontend:
- HTML
- CSS
- JavaScript

---

## 🎥 User Flow

1. Enter prompt  
2. Select style  
3. Generate video  
4. Observe live progress  
5. View final output  

---

## 🔮 Future Improvements

- Redis-backed job storage  
- Distributed task queues  
- WebSockets / SSE  
- Audio generation  

---

## 👨‍💻 Author

Devansh Trivedi

---

This project demonstrates how modern AI systems are designed to remain responsive even under slow, GPU-heavy inference workloads.
