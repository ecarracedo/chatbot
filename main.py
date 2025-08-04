
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar las variables de entorno
# Load environment variables
load_dotenv()
genai.configure = os.getenv("GEMINI_API_KEY")
if not genai.configure:
    raise ValueError("La clave API de Gemini no está configurada en las variables de entorno.")
# Configurar la API de Gemini
# Configure the Gemini API
generation_config={
        "temperature": 0.7,
        "max_output_tokens": 200,
        }
system_prompt = "Eres un asistente que odia las preguntas."

# Inicializar el modelo 
# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')
message = []


def chat (user_input):
    # Historial de conversación
    # Conversation history
    message.append('Usuario: ' + user_input)
    
    # Definir el prompt del sistema
    # Define the system prompt
    response = model.generate_content(
        [system_prompt, user_input],
        generation_config=generation_config
    )

    reply = ('Asistente: ' + response.text)
    message.append(reply)
    
    return reply

# Bucle de chat
# Chat loop
while True:
    user_input = input("Usuario: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Saliendo del chat.")
        break
    reply = chat(user_input)
    print(f"Usuario : {user_input}\n")
    print(f"Asistente: {reply}")


