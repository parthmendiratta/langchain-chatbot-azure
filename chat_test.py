import os
import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("AZURE_OPENAI_KEY", st.secrets.get("AZURE_OPENAI_KEY", None))
api_version = os.getenv("AZURE_OPENAI_API_VERSION", st.secrets.get("AZURE_OPENAI_API_VERSION", None))
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", st.secrets.get("AZURE_OPENAI_DEPLOYMENT", None))
api_base = os.getenv("AZURE_OPENAI_ENDPOINT", st.secrets.get("AZURE_OPENAI_ENDPOINT", None))

# Setup Streamlit
st.set_page_config(page_title="LangChain Chatbot", layout="centered")
st.title("🧠 LangChain Chatbot (Azure OpenAI)")

# Sidebar slider for temperature
temperature = st.sidebar.slider("Response Creativity (Temperature)", 0.0, 1.0, 0.7, 0.1)

# Initialize chat history and memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

if "chain" not in st.session_state:
    llm = AzureChatOpenAI(
        openai_api_key=openai_api_key,
        azure_endpoint=api_base,
        api_version=api_version,
        deployment_name=deployment_name,
        model="gpt-35-turbo",
        temperature=temperature
    )
    st.session_state.chain = ConversationChain(llm=llm, memory=st.session_state.memory)

# Elegant message rendering
for msg in st.session_state.memory.chat_memory.messages:
    if msg.type == "human":
        st.markdown(
            f"""
            <div style="background-color:#1e1e1e; color:#e0ffe0;
                        border: 1px solid #33ff33; border-radius: 12px;
                        padding: 10px 16px; margin-bottom: 12px; text-align: right;
                        font-family: 'Segoe UI', sans-serif; font-size: 16px;">
                <strong>You:</strong> {msg.content}
            </div>
            """, unsafe_allow_html=True
        )
    elif msg.type == "ai":
        st.markdown(
            f"""
            <div style="background-color:#1e1e1e; color:#ffe0e0;
                        border: 1px solid #ff3333; border-radius: 12px;
                        padding: 10px 16px; margin-bottom: 12px; text-align: left;
                        font-family: 'Segoe UI', sans-serif; font-size: 16px;">
                <strong>Bot:</strong> {msg.content}
            </div>
            """, unsafe_allow_html=True
        )

# Chat input at the bottom
user_input = st.chat_input("Type your message here...")

if user_input:
    response = st.session_state.chain.invoke({"input": user_input})
    st.rerun()
