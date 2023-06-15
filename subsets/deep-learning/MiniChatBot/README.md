# MiniChatBot (NLP + Speech Recognition)

## Overview
A real-time customer support chatbot built with:
- **Intent classification (NLP)** using a pretrained Keras model
- **Pattern/response dataset** stored in `commands.json`
- Optional **Speech-to-Text** input using `SpeechRecognition` + microphone

This bot listens (or accepts text), predicts an intent, and returns a matching response instantly.

---

## Project Structure
- `ChatBotScript.ipynb` — Run the chatbot (speech + text pipeline)
- `Create_ModelChatbot.ipynb` — Retrain the model (optional / if you change intents)
- `commands.json` — Intents dataset (`patterns` → `responses`)
- `chatbot_model.h5` — Trained model (binary)
- `words.pkl` — Vocabulary used by the model (binary)
- `classes.pkl` — Intent labels used by the model (binary)

---

## Setup

### 1) Create + activate a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate

2) Install dependencies
pip install numpy nltk tensorflow SpeechRecognition pyaudio
macOS microphone dependency (if pyaudio fails)
brew install portaudio
pip install pyaudio
NLTK Resources (first run)
Run this once in Python / notebook:
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")
Run the Chatbot
Open and run:
ChatBotScript.ipynb
Voice mode
Speak when prompted
Say exit to stop
Text-only mode (recommended for stability)
If you want text input only, use this loop in the notebook:
while True:
    msg = input("You: ")
    if msg.lower() in {"exit", "quit"}:
        break
    print("Bot:", chatbot_response(msg))
Notes / Common Issues

1) Don’t open .h5 or .pkl files in the editor
They are binary artifacts (they will look like garbage text).

2) File paths
Use relative paths (recommended) since all files are in the same folder:
chatbot_model.h5
commands.json
words.pkl
classes.pkl

3) Model input shape fix
This project’s model expects input shape (batch, time_steps, features).
If you see shape errors, ensure the prediction code uses:
(1, 1, 88) instead of (1, 88) (adds the missing time-step dimension).

