import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

class Mitra:
    HISTORY_FILE ="history.json"
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

    def __init__(self):
        self.client = OpenAI(
            api_key = os.getenv("GROQ_API_KEY"),
            base_url = "https://api.groq.com/openai/v1",
        )
        self.conversation_history = self.load_history()

    def load_history(self):
        if Path(self.HISTORY_FILE).exists():
            with open(self.HISTORY_FILE, "r") as f:
                return json.load(f)
        return[]

    def save_history(self):
        with open(self.HISTORY_FILE,"w") as f:
            json.dump(self.conversation_history,f)

    def clear_memory(self):
        self.conversation_history.clear()
        if Path(self.HISTORY_FILE).exists():
            os.remove(self.HISTORY_FILE)
        print("Memory cleared. Fresh start!\n")

    def chat(self,user_input):
        self.conversation_history.append({
            "role":"user",
            "content": user_input,
        })
        try:
            stream = self.client.chat.completions.create(
                model = "openai/gpt-oss-120b", 
                messages = [self.SYSTEM_PROMPT] + self.conversation_history,
                stream = True,
            )
            print("Mitra: ", end="", flush=True)
            reply = ""
            for chunk in stream:
                token = chunk.choices[0].delta.content or ""
                print(token, end="", flush=True)
                reply += token
            print("\n")
            self.conversation_history.append({
                "role": "assistant",
                "content":reply,
            })

        except Exception as e:
            print(f"Oops!, something went wrong : {e}\n")
            self.conversation_history.pop() # removes ghost message

    def run(self):
        print("Mitra is ready. Type 'exit' to quit or 'clear' to reset memory.\n")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                self.save_history()
                print("Goodbye!!")
                break
            elif user_input.lower() == "clear":
                self.clear_memory()
                continue
            self.chat(user_input)

if __name__ == "__main__":
    mitra = Mitra()
    mitra.run()