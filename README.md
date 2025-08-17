# Jarvis AI Chatbot 🤖

A simple voice-controlled AI assistant built with **Python**, powered by:
- Speech Recognition 🎙️
- Text-to-Speech (pyttsx3) 🗣️
- Google Gemini API (Generative AI) 🔮
- Web browsing & YouTube integration 🌐🎵

## ✨ Features
- **Voice activation**: Say "Jarvis" to wake the assistant.
- **Open websites**: e.g., "open google" → opens google.com.
- **Play songs on YouTube**: e.g., "play despacito".
- **Google search**: e.g., "search machine learning".
- **Chatbot mode**: Any other queries are answered using Google Gemini AI.

## 🛠️ Requirements
- Python 3.9+
- Working microphone 🎤
- Internet connection 🌍
- Google Gemini API key (replace in `main.py`)

## 🚀 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Jarvis-AI.git
   cd Jarvis-AI

2. Install dependencies:
      pip install -r requirements.txt

🔑 Setup Google Gemini API

Get an API key from Google AI Studio.

Open main.py and replace:

genai.configure(api_key="YOUR_API_KEY")


📌 Example Commands

"Jarvis, open YouTube"

"Jarvis, play Believer"

"Jarvis, search Python tutorials"

"Jarvis, tell me a joke"
