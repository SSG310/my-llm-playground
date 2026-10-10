# Mitra — Your Desi AI Companion 🤖

A CLI chatbot powered by Groq's LLM API, built with Python.  
Mitra is friendly, a little Desi, and remembers your conversations across sessions.

---

## Features

- 💬 Streaming responses — words appear as they're generated
- 🧠 Persistent memory — remembers context across sessions via JSON
- 🧹 Clear memory — type `clear` to start fresh
- ⚠️ Error handling — gracefully handles API failures
- 🏗️ Clean OOP structure — built as a Python class

---

## Tech Stack

- Python 3
- [Groq API](https://console.groq.com) — free LLM inference
- `openai` SDK (OpenAI-compatible)
- `python-dotenv` for environment variables

---

## Setup

1. Clone the repo
```bash
   git clone https://github.com/SSG310/my-llm-playground.git
   cd my-llm-playground
```

2. Create and activate a virtual environment
```bash
   python -m venv .venv
   source .venv/bin/activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Add your Groq API key
```bash
   # create a .env file
   echo "GROQ_API_KEY=your-key-here" > .env
```

5. Run Mitra
```bash
   python main.py
```

---

## Commands

| Command | What it does |
|---------|--------------|
| `exit`  | Save history and quit |
| `clear` | Wipe memory and start fresh |

---

## Project Structure
my-llm-playground/
├── main.py # Mitra chatbot class
├── .env # API key (not tracked)
├── .gitignore
├── history.json # Auto-generated, not tracked
└── README.md

---

## Built by

Snehanshu Gunjal — [GitHub](https://github.com/SSG310) · [LinkedIn](https://linkedin.com/in/snehanshu-gunjal)