# 🎬 Cinema Booking with Grok, LLaMA2 & Gem AI

An intelligent **cinema ticket booking system** powered by **Large Language Models (LLMs)**, **tool calling**, and **Gem AI** for human-like interactions.  
This project combines traditional APIs with conversational AI, enabling users to log in, chat naturally, and perform tasks like **ticket booking, movie rescheduling, and payments** through simple dialogue.  

---

## ✨ Features

- 🔑 **User Authentication** – Secure login & signup system.  
- 💬 **Conversational Booking** – Interact with an LLM chatbot (Grok / LLaMA2).  
- 🛠 **Tool Calling** – Backend functions for:  
  - Movie ticket booking  
  - Rescheduling  
  - Payments  
  - Greetings & other utilities  
- 🧠 **Gem AI Integration** – Humanizes LLM outputs, making them more natural and engaging.  
- 🧪 **API Testing with Postman** – Pre-configured collection for testing endpoints.  

---

## 🏗 System Architecture

```mermaid
flowchart TD
    A[User Login] --> B[LLM (Grok / LLaMA2)]
    B -->|Tool Call| C[FastAPI Backend]
    C -->|book_ticket, reschedule_ticket, payment| D[Database]
    C --> E[Return JSON Response]
    E --> F[Gem AI Humanizer]
    F --> G[Final Human-like Reply]
