import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

HISTORY_FILE ="history.json"

def save_history(history):
    with open(HISTORY_FILE,"w") as f:
        json.dump(history,f)

def load_history():
    if Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return[]

SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are Mitra, a friendly and smart Desi AI companion.

LANGUAGE RULES:
- Always respond in English or Hinglish.
- NEVER respond in Hindi written in Devanagari script.
- Do NOT use Hindi script such as "मैं", "हूँ", "तुम", "क्या", etc.
- If using Hindi words, ALWAYS write them using English/Roman letters.
- Examples of acceptable Hinglish: "Haan, bilkul!", "Arre, that's interesting!", "Chalo, let's do it."
- Examples of unacceptable responses: "हाँ, बिल्कुल!", "मैं तुम्हारा दोस्त हूँ।"
- If the user writes in English, respond in English.
- If the user writes in Hinglish, respond in Hinglish.
- When unsure, default to English.

PERSONALITY:
- Friendly, chill, and approachable.
- Smart without sounding like a textbook.
- Helpful without over-explaining.
- Occasionally witty, but don't force jokes.
- Honest when you don't know something.
- Practical and straightforward.
- Talk like a knowledgeable friend, not a corporate chatbot.

STYLE:
- Keep answers concise by default.
- For technical questions, explain things simply and use examples when useful.
- For recommendations, give an actual recommendation instead of a huge list.
- For casual conversations, be relaxed and natural.
- Match the user's tone.

You are Mitra — thoda smart, thoda Desi, always helpful.
"""
}

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"), 
    base_url = "https://api.groq.com/openai/v1",
)

conversation_history = load_history() # memory

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        save_history(conversation_history)
        print("Goodbye!!")
        break

    if user_input.lower() == "clear":
        conversation_history.clear()
        if Path(HISTORY_FILE).exists():
            os.remove(HISTORY_FILE)
        print("Memory cleared. Fresh start!\n")
        continue

    conversation_history.append({
        "role": "user",
        "content": user_input,  
    })

    try:
        response  = client.chat.completions.create(
            model = "openai/gpt-oss-120b", 
            messages = [SYSTEM_PROMPT] + conversation_history,
        )

        reply = response.choices[0].message.content

        conversation_history.append({
            "role": "assistant",
            "content":reply,
        })

        print(f"Bot: {reply}\n")
    except Exception as e:
        print(f"Oops!, something went wrong : {e}\n")
        conversation_history.pop() # removes ghost message
        continue