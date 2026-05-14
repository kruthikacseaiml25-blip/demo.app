import streamlit as st
from openai import OpenAI

# OpenAI client
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# App title
st.title("Simple AI Chatbot")

# User input
user_input = st.text_input("Ask something:")

if st.button("Send"):

    if user_input:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content

        st.write("AI Response:")
        st.success(answer)
