import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"), 
    base_url = "https://api.groq.com/openai/v1",
)

converstaion_history = [] # memory

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!!")
        break

    converstaion_history.append({
        "role": "user",
        "content": user_input,  
    })

    response  = client.chat.completions.create(
        model = "openai/gpt-oss-120b", 
        messages = converstaion_history,
)

    reply = response.choices[0].message.content

    converstaion_history.append({
        "role": "assistant",
        "content":reply,
})

    print(f"Bot: {reply}\n")