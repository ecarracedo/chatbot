import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("La clave API de Gemini no está configurada en las variables de entorno.")

genai.configure(api_key=GEMINI_API_KEY)

print("Modelos disponibles:")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(f"- {m.name} (Compatible con generateContent)")