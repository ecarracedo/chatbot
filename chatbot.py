# chatbot_langchain.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar las variables de entorno 
# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY no encontrada")

# Configurar la API de Gemini
# Configure the Gemini API
genai.configure(api_key=api_key)
generation_config = {
    "temperature": 0.7,
    "max_output_tokens": 200,
}

# Inicializar el modelo
# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')


class ChatBot:

    # Inicializar el chatbot con una personalidad
    # Initialize the chatbot with a personality
    def __init__(self, personalidad):
        self.personalidad = personalidad
        self.history = []

    # Método para chatear con el modelo
    # Method to chat with the model
    def chat(self, user_input: str, idioma: str = "Español") -> str:

        # Definir el prompt del sistema según el idioma y la personalidad
        # Define the system prompt based on the language and personality
        
        prompt_idioma = "Responde en español." if idioma == "Español" else "Respond in English."
        system_prompt = f"{prompt_idioma} Tu personalidad es: {self.personalidad}"

        self.history.append(f"Usuario: {user_input}")

        response = model.generate_content(
            [system_prompt, user_input],
            generation_config=generation_config
        )

        reply = response.text
        self.history.append(f"Asistente: {reply}")
        return reply
