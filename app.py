import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Please add your GEMINI_API_KEY to the .env file")
    st.stop()

genai.configure(api_key=api_key)

# Initialize the model - using the free Gemini 2.0 Flash model
model = genai.GenerativeModel('models/gemini-2.0-flash')

# Set page config
st.set_page_config(
    page_title="Gen AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# App title
st.title("🤖 Gen AI Chatbot")
st.caption("Powered by Google Gemini")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response
        response = st.session_state.chat.send_message(prompt, stream=True)
        
        for chunk in response:
            if chunk.text:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with options
with st.sidebar:
    st.header("Settings")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    st.subheader("About")
    st.info(
        "This is a Gen AI chatbot built with Streamlit and Google Gemini. "
        "Ask any question and get intelligent responses!"
    )
    
    st.subheader("Setup")
    st.markdown("""
    1. Add your Gemini API key to `.env` file
    2. Run: `uv sync` to install dependencies
    3. Run: `streamlit run app.py`
    """)
