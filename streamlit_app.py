import streamlit as st
import os
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key=("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"),
)

def get_chat_response(user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

def main():
    st.title("Chatbot")
    user_input = st.text_input("Welcome to this Chatbot:")
    if st.button("Send"):
        response = get_chat_response(user_input)
        st.write(f"Bot: {response}")

if __name__ == "__main__":
    main()



# streamlit run streamlit_app.py