# 📈 Market Sentiment Tracker

A high-performance, full-stack data pipeline that quantifies market psychology. This app fetches real-time financial news for any ticker (Stocks or Crypto) and uses Natural Language Processing (NLP) to determine if the current market mood is **Bullish**, **Bearish**, or **Neutral**.

## 🚀 Live Features
* **Real-time News Ingestion:** Connects to Alpha Vantage API for the latest financial headlines.
* **Sentiment Analysis:** Utilizes `TextBlob` (NLP) to calculate polarity scores for every headline.
* **Interactive Dashboard:** Built with `Streamlit` for clean, professional data visualization.
* **Asynchronous Backend:** Powered by `FastAPI` to handle I/O-bound API requests efficiently.
* **Quality Assurance:** Includes a `Pytest` suite to ensure data integrity and logic accuracy.

---

## 🛠️ The Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** Streamlit, Pandas
* **NLP:** TextBlob (Sentiment Polarity)
* **Testing:** Pytest, HTTPX (TestClient)
* **DevOps:** GitHub Actions (CI/CD), Docker

---

## 🏗️ System Architecture

1. **Data Layer:** The user inputs a ticker (e.g., NVDA). The system fetches the 10 most recent news articles via the Alpha Vantage News Sentiment API.
2. **Analysis Layer:** The FastAPI backend processes each headline through an NLP pipeline, assigning a score from -1.0 (Panic) to +1.0 (Euphoria).
3. **Presentation Layer:** The Streamlit frontend aggregates these scores into a "Market Intelligence Report" with color-coded sentiment drivers.

---

## 🧪 Engineering Highlights (The "Why")

### 1. Separation of Concerns
Instead of building a monolithic script, I separated the **Intelligence Engine (FastAPI)** from the **UI (Streamlit)**. This allows the backend to be scaled independently or consumed by other services (like a Discord bot or a mobile app).

### 2. Automated CI/CD Pipeline
I implemented **GitHub Actions** to automate testing. Every time code is pushed to the `main` branch, the test suite runs automatically to ensure the NLP logic hasn't regressed.

### 3. Handling API Constraints
To manage Alpha Vantage's free-tier rate limits, I engineered the backend to be **asynchronous**, preventing the UI from hanging while waiting for third-party data.


   ```bash
   git clone [https://github.com/Edi109/market-sentiment-tracker.git](https://github.com/edi109/market-sentiment-tracker.git)
   cd market-sentiment-tracker