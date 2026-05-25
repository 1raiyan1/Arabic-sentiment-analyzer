import streamlit as st
import requests

st.title("Arabic + English Sentiment Analyzer")

text = st.text_area(
    "Enter Arabic or English text"
)

if st.button("Analyze"):

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={"text": text}
    )

    result = response.json()

    st.write(result["result"])