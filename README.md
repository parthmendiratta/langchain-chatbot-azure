# 💬 LangChain Chatbot with Azure OpenAI + Streamlit

This project is a simple, fully working AI chatbot built using **LangChain**, **Streamlit**, and **Azure OpenAI (GPT-3.5 Turbo)**. It provides a clean UI for interacting with an intelligent assistant, and it's structured to be easily extended for advanced use cases like memory, tools, or RAG.

---

## 🚀 Features

- ✨ Built with `LangChain` and `AzureOpenAI`
- 🌐 Frontend with `Streamlit` for clean and interactive UI
- 🔐 Secure API key handling using `.streamlit/secrets.toml`
- 🧠 Uses the `invoke()` method from `LangChain` for single-turn chat
- 💡 Easily extendable to support memory, RAG, and tool integrations

---

## 🗂️ Project Structure

```
langchain-chatbot/
│
├── chat_test.py              # Main Streamlit app
├── .streamlit/
│   └── secrets.toml          # Stores your Azure API keys (do NOT upload publicly)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/parthmendiratta/langchain-chatbot-azure.git
cd langchain-chatbot
```

### 2. Set Up Environment

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Add API Keys

Create a file called `.streamlit/secrets.toml` and add the following:

```toml
[azure]
openai_api_key = "your-azure-openai-key"
openai_api_base = "https://your-endpoint.openai.azure.com/"
openai_api_version = "2025-01-01-preview"
deployment_name = "gpt-35-turbo"
```

> ⚠️ **Never upload `secrets.toml` to GitHub.** It's already ignored via `.gitignore`.

---

## 🧪 Run Locally

```bash
streamlit run chat_test.py
```

---

## 🌐 Live Demo

Once deployed on Streamlit Cloud, update the link here:

🔗 [View Live Chatbot](https://langchain-chatbot-azure-adbtboffypdkgbsw9fhiro.streamlit.app/)

---

## 🙌 Author

Made with ❤️ by [Parth Mendiratta](https://github.com/parthmendiratta)

---

## ⭐ Like This Project?

If this saved you time or taught you something, consider starring 🌟 the repo!
