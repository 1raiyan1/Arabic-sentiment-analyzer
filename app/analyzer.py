from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def analyze_sentiment(text):

    prompt = f"""
    Detect language first.
    Analyze sentiment.

    Return:

    Language:
    Sentiment:
    Confidence:
    Reason:

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content