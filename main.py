
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("La clave API de Gemini no está configurada en las variables de entorno.")

client = genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content([
    "You are a helpful assistant.",
    "What is the capital of France?"
])


print(response.text)

