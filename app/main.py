from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment import analyze_sentiment

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analyzer API!"}

@app.post("/analyze/")
def analyze_text_sentiment(request: TextRequest):
    result = analyze_sentiment(request.text)
    return {"sentiment": result}
