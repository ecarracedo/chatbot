import streamlit as st
from chatbot_langchain import ChatBot

PERSONALIDADES = {
    "Español": {
        "Neutral": "Eres un asistente amable y educado.",
        "Pirata": "Hablas como un pirata del Caribe, usando jerga marinera.",
        "Terminator": "Respondes como Terminator, con tono robótico y sin emociones.",
        "Yoda": "Hablas como el maestro Yoda, con frases invertidas.",
        "Hater": "Odias las preguntas. Respondes con sarcasmo y molestia."
    },
    "English": {
        "Neutral": "You are a friendly and polite assistant.",
        "Pirate": "You speak like a Caribbean pirate, using pirate slang.",
        "Terminator": "You answer like Terminator: robotic, emotionless, direct.",
        "Yoda": "You talk like Master Yoda, in inverted phrases.",
        "Hater": "You hate questions. You're sarcastic and annoyed."
    }
}

st.set_page_config(page_title="Chat con Personalidad", layout="centered")
st.title("🌍 Chat con Personalidad Multilingüe")

idioma = st.selectbox("Elige un idioma / Choose a language:", ["Español", "English"])
modo = st.selectbox("Elige una personalidad / Choose a personality:", list(PERSONALIDADES[idioma].keys()))
descripcion = PERSONALIDADES[idioma][modo]

# Inicializar si es necesario
if (
    "chatbot" not in st.session_state
    or st.session_state.modo != modo
):
    st.session_state.chatbot = ChatBot(descripcion)
    st.session_state.modo = modo
    st.session_state.chat_history = []

# Mostrar historial
for speaker, msg in st.session_state.chat_history:
    with st.chat_message(speaker):
        st.markdown(msg)

# Entrada
if prompt := st.chat_input("Tu mensaje / Your message"):
    with st.chat_message("user"):
        st.markdown(prompt)

    respuesta = st.session_state.chatbot.chat(prompt, idioma)

    with st.chat_message("assistant"):
        st.markdown(respuesta)

    st.session_state.chat_history.append(("user", prompt))
    st.session_state.chat_history.append(("assistant", respuesta))