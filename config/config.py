import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROG_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")