
import streamlit as st
import random
import time

st.set_page_config(page_title="Insurance Chatbot", page_icon="🛡️")

st.markdown("""
    <style>
    .main {
        background-color: #f5f9fc;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextInput>div>div>input {
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #d0d7de;
    }
    </style>
""", unsafe_allow_html=True)

def fake_bot_response(user_input):
    responses = [
        "That's a great question! Here's what you need to know...",
        "Sure! Let me break it down for you.",
        "Absolutely! Here's some helpful info on that.",
        "This is how the insurance process works in your case...",
        "Let me explain how coverage applies to that situation."
    ]
    escalation_chance = random.choice([False, False, False, True])
    message = random.choice(responses)
    if escalation_chance:
        message += "\n\n🔁 Your query may need a human agent. We've forwarded it for you."
    return message

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown("""
<div style='text-align: center;'>
    <h2>🛡️ Insurance Policy Chatbot</h2>
    <p style='font-size: 16px; color: gray;'>
        Ask about health, life, auto, or home insurance.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input("Ask a question", placeholder="e.g. How can I claim car insurance?", label_visibility="collapsed", key="input")
with col2:
    send = st.button("Send")

if send and user_input:
    st.session_state.chat_history.append(("You", user_input))
    with st.spinner("Thinking..."):
        time.sleep(1.5)
        bot_reply = fake_bot_response(user_input)
        st.session_state.chat_history.append(("Bot", bot_reply))
        st.session_state.input = ""

for speaker, message in reversed(st.session_state.chat_history):
    with st.chat_message(name=speaker):
        st.markdown(message)

st.divider()
st.markdown("""
<p style='text-align: center; font-size: 12px; color: #999;'>
This is a UI demo — responses are simulated. Connect to an AI backend to go live!
</p>
""", unsafe_allow_html=True)
