# 🤖 Multilingual Personality Chatbot

This project is an interactive chatbot application built with **Streamlit** and **LangChain**, using Google’s **Gemini** model to generate responses based on the personality chosen by the user for the LLM. It also allows the user to select the response language, making the experience more fun or themed.

## ✨ Main Technologies

- Streamlit
- LangChain
- Gemini

## 🚀 Features

- Supported languages: Spanish 🇪🇸 and English 🇬🇧
- Available personalities:
  - Neutral
  - Pirate 🏴‍☠️
  - Terminator 🤖
  - Yoda 🧙
  - Hater 😠
- Session-persistent chat history
- Integration with Gemini (Google Generative AI) through LangChain

## 📁 Project Structure

```
├── app.py                   # Main Streamlit application
├── chatbot_langchain.py     # Chatbot logic using LangChain and Gemini
├── .env                     # Environment variables (Gemini API key)
```

## 🧠 Requirements

- Python 3.13+
- Install libraries from `requirements.txt`
- A [Google AI Studio](https://aistudio.google.com/app/apikey) account to get your Gemini API key
- Create a `.env` file in the root folder with the environment variable to configure the API KEY

```
GEMINI_API_KEY='YOUR API KEY'
```

### 📦 Main Dependencies

```bash
pip install streamlit python-dotenv langchain langchain-google-genai
```

## 🔑 Setup

Create a `.env` file in the same directory as `chatbot_langchain.py` and add your API key:

```env
GEMINI_API_KEY=your_api_key
```

## 🏃‍♂️ How to Run

From the terminal, run:

```bash
streamlit run app.py
```

This will open the interface in your default browser, where you can chat with the assistant.

## ✨ Example Usage

1. Select the language (Español or English).
2. Choose a personality.
3. Type your message and the chatbot will respond in the selected style.

```
https://chatbot-personality.streamlit.app/
```

## 📌 Technical Notes

- Conversation history is stored in memory per session using LangChain’s `RunnableWithMessageHistory`.
- The model used is `gemini-1.5-flash`, configured with `temperature 0.7` (0 = more deterministic, 1 = more creative).
- Responses are guided by a custom system message that defines both language and personality.
- This project is adaptable for `ChatGPT`. You only need to adapt the `chat` function in the `ChatBot` class to match your desired LangChain configuration.

## 🎭 Adding Personalities

To add more personalities, simply update the `PERSONALIDADES` dictionary in the `app.py` file for both Spanish and English:

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

## ✨ Extra Files

- The files `models-chatgpt.py` and `models-gemini.py` are scripts used to list the available models depending on the country where they're run. Use them if your chosen model isn't working, to check what's available.
- The files `main.py` and `chatbot.py` are earlier versions that evolved into the final `chatbot_langchain.py`. They are included to show the transition from raw code to a LangChain implementation.

## 🧠 What Was Learned From This Project?

Through the development of this project, I gained hands-on experience with several key technologies and concepts in AI-based application development:

✅ `Streamlit`: Building dynamic and interactive web interfaces rapidly and efficiently.

✅ `LangChain`: Implementing LLM chains, prompt templates, and persistent chat memory via `RunnableWithMessageHistory`.

✅ `Google Gemini (Generative AI)`: Integration of a state-of-the-art LLM (Gemini 1.5 Flash) through API access and environment variables.

✅ `Prompt engineering`: Designing flexible prompts that adapt to user-selected language and personality settings.

✅ `Session-based memory`: Maintaining conversational context using `InMemoryChatMessageHistory`.

✅ `Multilingual design`: Allowing language switching (Spanish/English) and ensuring the AI responds accordingly.

✅ `Scalability and extensibility`: Creating a structure that makes it easy to add new personalities or switch LLM providers (e.g., from Gemini to ChatGPT).

This project also provided a deeper understanding of how to personalize AI responses and simulate character-like behavior, making chatbots more engaging and versatile.

## 📜 License

This project is free to use for educational and development purposes.

Developed by Emiliano Carracedo | ecarracedo@gmail.com |

