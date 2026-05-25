from groq import Groq

def analyze_sentiment(text, api_key):
    client = Groq(api_key=api_key)

    prompt = f"""
    Detect language first.
    Analyze sentiment.

    Return:

    Language:
    Sentiment:
    Confidence:
    Reason:
    Translation (if Arabic):

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