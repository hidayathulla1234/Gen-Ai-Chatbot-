from dotenv import load_dotenv
import streamlit as st
import os 
from langchain_groq import ChatGroq

# load env variables
load_dotenv()

# Get API Key
groq_api_key = os.environ["GROQ_API_KEY"]="gsk_VN8H3zILixZDPsOsF2NcWGdyb3FYSmhAb8OqOGWTBr9vy3SGGzhAgt"

# streamlit page setup
st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Generative AI ChatBot")

# initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0
)

# user input
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:

    # show user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # save user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_prompt
    })

    # create messages list
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant"
        }
    ] + st.session_state.chat_history

    # get response
    response = llm.invoke(messages)

    assistant_response = response.content

    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # save assistant response
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_response
    })
