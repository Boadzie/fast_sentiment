import uvicorn
from fastapi import FastAPI

api = FastAPI(title="Fast_Sentiment - Sentimental Analyzer API")


@api.get("/")
def home():
    return {"Message": "Welcome to Fast_Sentiment!"}


# run the API
if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8080)
