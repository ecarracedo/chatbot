
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure = os.getenv("GEMINI_API_KEY")
if not genai.configure:
    raise ValueError("La clave API de Gemini no está configurada en las variables de entorno.")

generation_config={
        "temperature": 0.7,
        "max_output_tokens": 200,
        }
system_prompt = "Eres un asistente que odia las preguntas."
model = genai.GenerativeModel('gemini-2.0-flash')
message = []


def chat (user_input):

    message.append('Usuario: ' + user_input)
    
    response = model.generate_content(
        [system_prompt, user_input],
        generation_config=generation_config
    )

    reply = ('Asistente: ' + response.text)
    message.append(reply)
    
    #print(message)

    return reply

while True:
    user_input = input("Usuario: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Saliendo del chat.")
        break
    reply = chat(user_input)
    print(f"Usuario : {user_input}\n")
    print(f"Asistente: {reply}")


