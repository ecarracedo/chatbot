# 🤖 Chat con Personalidad Multilingüe


Este proyecto es una aplicación de chatbot interactivo construida con **Streamlit** y **LangChain**, que utiliza el modelo de Google **Gemini** para generar respuestas en base a la personalidad que el usuario elija para el modelo LLM, haciendo la experiencia más divertida o temática. A su vez tambien puede seleccionar el idioma de respuesta.

## 🚀 Características

- Idiomas soportados: Español 🇪🇸 y English 🇬🇧
- Personalidades disponibles:
  - Neutral
  - Pirata 🏴‍☠️
  - Terminator 🤖
  - Yoda 🧙
  - Hater 😠
- Chat con historial persistente por sesión
- Integración con Gemini (Google Generative AI) a través de LangChain

## 📁 Estructura del Proyecto

```
├── app.py                   # Aplicación principal con Streamlit
├── chatbot_langchain.py     # Lógica del chatbot usando LangChain y Gemini
├── .env                     # Variables de entorno (API key de Gemini)
```

## 🧠 Requisitos

- Python 3.13+
- Instalar las librerias desde `requeriments.txt`
- Una cuenta en [Google AI Studio](https://aistudio.google.com/app/apikey) para obtener la API Key de Gemini
- Crear una un archivo .env con la variable de entorno para configurar el API KEY

```
GEMINI_API_KEY='TU API KEY'
```

### 📦 Dependencias principales

```bash
pip install streamlit python-dotenv langchain langchain-google-genai
```

## 🔑 Configuración

Crea un archivo `.env` en el mismo directorio que `chatbot_langchain.py` y agrega tu API key:

```env
GEMINI_API_KEY=tu_clave_api
```

## 🏃‍♂️ Cómo ejecutar

En la terminal, ejecuta:

```bash
streamlit run app.py
```

Esto abrirá la interfaz en tu navegador predeterminado, donde podrás chatear con el asistente.

## ✨ Ejemplo de uso

1. Selecciona el idioma (Español o English).
2. Elige una personalidad.
3. Escribe tu mensaje y el chatbot responderá con el estilo elegido.


## 📌 Notas Técnicas

- El historial de conversación se guarda en memoria por sesión mediante `RunnableWithMessageHistory` de LangChain.
- El modelo usado es `gemini-1.5-flash` configurado con `temperatura 0.7` (0 mas deterministico y 1 mas).
- Las respuestas son controladas por un mensaje del sistema personalizado que define idioma y personalidad.
- Este proyecto es adaptable para `ChatGPT` solo hay que adaptar la funcion `chat` de la clase `ChatBot` a la configuracion del modelo segun los parametros de `Langchain`.


## Personalidades

Para agregar mas personalidades, solamente debera agregar las mismas dentro del archivo `app.py`, tanto en Español como en Ingles.

```
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
```
## ✨ Archivos Extras

- Los archivos `models-chatgpt.py` y `models-gemini.py` son scripts que sirven para listar los modelos que estan accesibles dependiendo del pais donde se ejecuten. Esto es si desean cambiar el modelo y no les funcionas, verificar los modelos con este scripts.
- Los archivos `main.py` y `chatbot.py` son archivos previos que fueron cambiando para la version final de `chatbot_langchain.py`. Los he dejado para que vean la como empezo este proyecto.

## 📜 Licencia

Este proyecto es de uso libre para fines educativos y de desarrollo.
