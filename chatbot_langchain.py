import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import SystemMessage
from typing import Dict

# Cargar variables de entorno
# Load environment variables
load_dotenv()

# Obtener API Key
# Obtain API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY no encontrada en las variables de entorno")

# Inicializar el modelo
# Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0.7,
    google_api_key=api_key
)

# Almacén de historial por sesión
# Session history store
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


class ChatBot:
    def __init__(self, personalidad: str):
        self.personalidad = personalidad

    def chat(self, user_input: str, idioma: str = "Español", session_id: str = "default") -> str:
        # Definir el mensaje del sistema según idioma
        # Define the system message based on language
        idioma_prompt = "Responde en español." if idioma == "Español" else "Respond in English."
        system_content = f"{idioma_prompt} Tu personalidad es: {self.personalidad}"

        # Crear el prompt con mensaje del sistema + historial + entrada
        # Create the prompt with system message + history + input
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_content),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        # Crear la cadena (LCEL)
        # Create the chain (LCEL)
        chain = prompt | llm

        # 4. Wrap con historial persistente
        chat = RunnableWithMessageHistory(
            chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )

        # 5. Invocar con ID de sesión (para mantener conversación)
        response = chat.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )

        # 6. Devolver solo el contenido de la respuesta
        return response.content