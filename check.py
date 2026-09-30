import os
from dotenv import load_dotenv
load_dotenv()
key_name = "GROQ_API_KEY"
key_exists = bool(os.getenv(key_name))
print(f"Key exists : {key_exists}")