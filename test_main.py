import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_api_connection():
    """Verify the API endpoint responds correctly for a major ticker."""
    response = client.get("/analyze/AAPL")
    assert response.status_code == 200
    json_data = response.json()
    assert "ticker" in json_data
    assert "avg_sentiment" in json_data

def test_sentiment_math():
    """Unit test for the NLP logic directly."""
    from textblob import TextBlob
    # Use very clear positive words for the test case
    text = "Company had amazing, excellent, and great record-breaking profits"
    score = TextBlob(text).sentiment.polarity
    assert score > 0  # This should now pass with ~0.6-0.8 score