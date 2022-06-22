import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api = FastAPI(title="Fast_Sentiment - Sentimental Analyzer API")


class TextInput(BaseModel):
    text: str


@api.get("/")
def home():
    return {"Message": "Welcome to Fast_Sentiment!"}


@api.post("/sentiment")
async def get_sentiment(input: TextInput):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(input.text)
    sentiment = None
    if result["compound"] >= 0.05:
        sentiment = "Positive"
    elif result["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return {
        "result": f"The sentiment of the text is: {sentiment} and the confident score is {round(result['compound'], 2)*100}%"
    }


# run the API
if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8080)
