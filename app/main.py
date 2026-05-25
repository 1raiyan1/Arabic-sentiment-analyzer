from fastapi import FastAPI
from pydantic import BaseModel
from app.analyzer import analyze_sentiment

app = FastAPI()

class TextInput(BaseModel):
    text: str
    api_key: str

@app.post("/analyze")
def analyze(data: TextInput):
    result = analyze_sentiment(data.text, data.api_key)
    return {"result": result}