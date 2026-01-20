import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.title("🧠 SafeSpace – AI Mental Health Therapist")

if "chat" not in st.session_state:
    st.session_state.chat = []

msg = st.chat_input("What's on your mind?")
if msg:
    st.session_state.chat.append(("user", msg))
    res = requests.post(BACKEND_URL, json={"message": msg}).json()
    st.session_state.chat.append(("assistant", res["response"]))

for role, text in st.session_state.chat:
    with st.chat_message(role):
        st.write(text)
