import streamlit as st
import requests

st.title("Arabic + English Sentiment Analyzer")

api_key = st.text_input("Enter your Groq API Key", type="password")

text = st.text_area("Enter Arabic or English text")

if st.button("Analyze"):
    if not api_key:
        st.error("Please enter your Groq API key!")
    elif not text:
        st.error("Please enter some text!")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post(
                "https://arabic-sentiment-analyzer.onrender.com/analyze",
                json={"text": text, "api_key": api_key}
            )
            result = response.json()
            st.write(result["result"])