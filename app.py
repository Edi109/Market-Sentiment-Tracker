import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, HTTPException
import httpx
from textblob import TextBlob
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MarketPulse API", version="1.0.0")

# Enable CORS to allow the Streamlit frontend to communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use an environment variable for the API key for security
API_KEY = os.getenv("ALPHA_VANTAGE_KEY", "YOUR_FREE_KEY_HERE")
BASE_URL = "https://www.alphavantage.co/query"

@app.get("/analyze/{ticker}")
async def get_sentiment(ticker: str):
    """
    Fetches real-time news for a ticker and calculates an aggregate sentiment score.
    """
    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": ticker.upper(),
        "apikey": API_KEY
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(BASE_URL, params=params, timeout=10.0)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Data provider error: {str(e)}")

    feed = data.get("feed", [])
    if not feed:
        return {
            "ticker": ticker.upper(),
            "avg_sentiment": 0,
            "label": "No Data Found",
            "headlines": []
        }

    # NLP Processing Loop
    results = []
    scores = []
    
    for item in feed[:10]:  # Analyze top 10 headlines for efficiency
        text = item.get("title", "")
        # TextBlob returns polarity from -1.0 (Negative) to 1.0 (Positive)
        sentiment_score = TextBlob(text).sentiment.polarity
        scores.append(sentiment_score)
        results.append({"title": text, "score": round(sentiment_score, 2)})

    avg_score = sum(scores) / len(scores) if scores else 0
    
    # Determine Sentiment Category
    label = "Neutral"
    if avg_score > 0.15: label = "Bullish"
    elif avg_score < -0.15: label = "Bearish"

    return {
        "ticker": ticker.upper(),
        "avg_sentiment": round(avg_score, 3),
        "label": label,
        "headlines": results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)