# ==========================================================
# Weather Chatbot - Streamlit App
# ==========================================================

import streamlit as st

# Import chatbot response function
from chatbot.response import get_response

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Weather Chatbot",
    page_icon="🌦",
    layout="centered"
)

# ==========================================================
# Title
# ==========================================================

st.title("🌦 Intelligent Weather Chatbot")

st.markdown(
    "Ask me anything about the weather!"
)

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("Settings")

city = st.sidebar.text_input(
    "Enter City",
    value="Hyderabad"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "This chatbot predicts your intent using an LSTM model and retrieves live weather information from OpenWeather."
)

# ==========================================================
# Chat History
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================================
# Display Previous Messages
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ==========================================================
# Chat Input
# ==========================================================

user_input = st.chat_input("Ask a weather question...")

# ==========================================================
# Generate Response
# ==========================================================

if user_input:

    # Show User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get Bot Response
    bot_response = get_response(
        user_input,
        city
    )

    # Save Bot Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_response
        }
    )

    # Display Bot Response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# ==========================================================
# Clear Chat Button
# ==========================================================

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()