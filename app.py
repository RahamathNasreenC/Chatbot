import os
import streamlit as st
import google.generativeai as genai

# 🔑 Put your Gemini API key here
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Please set your GEMINI_API_KEY as an environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit App
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f4f7f9;
        }
        .main-title {
            text-align: center;
            font-size: 32px !important;
            color: #333333;
            margin-bottom: 20px;
        }
        .chat-container {
            max-height: 500px;
            overflow-y: auto;
            padding: 15px;
            border-radius: 12px;
            background-color: white;
            border: 1px solid #ddd;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        .user-bubble {
            background-color: #4CAF50;
            color: white;
            padding: 10px 14px;
            border-radius: 18px;
            margin: 8px;
            text-align: right;
            max-width: 70%;
            margin-left: auto;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
        .bot-bubble {
            background-color: #EAEAEA;
            color: black;
            padding: 10px 14px;
            border-radius: 18px;
            margin: 8px;
            text-align: left;
            max-width: 70%;
            margin-right: auto;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
        .stTextArea textarea {
            border-radius: 10px !important;
            border: 1px solid #ccc;
        }
        .stButton>button {
            border-radius: 10px;
            background: #4CAF50;
            color: white;
            padding: 8px 20px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)

# Store chat history in session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for role, text in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"<div class='user-bubble'>🧑 {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'>🤖 {text}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# User input at bottom
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area("💬 Type your message:", "", height=80)
    submitted = st.form_submit_button("Send")

    if submitted and user_input.strip() != "":
        # Generate response
        response = model.generate_content(user_input)

        # Save conversation
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response.text))
        st.rerun()
