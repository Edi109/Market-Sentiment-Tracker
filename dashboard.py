import streamlit as st
import requests
import pandas as pd

# Page Configuration for a professional look
st.set_page_config(page_title="MarketPulse AI", page_icon="📈", layout="wide")

st.title("📈 Market Sentiment Tracker")
st.markdown("---")

# Sidebar for inputs and info
st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter Asset Ticker (e.g. NVDA, BTC, TSLA):", "NVDA").upper()
analyze_btn = st.sidebar.button("Run Intelligence Report")

if analyze_btn:
    with st.spinner(f"Analyzing sentiment for {ticker}..."):
        try:
            # Request data from the FastAPI backend
            response = requests.get(f"http://localhost:8000/analyze/{ticker}")
            data = response.json()

            if data['label'] == "No Data Found":
                st.warning(f"No recent news found for {ticker}. Please check the ticker symbol.")
            else:
                # Top Level Metrics
                col1, col2, col3 = st.columns(3)
                col1.metric("Ticker", data['ticker'])
                col2.metric("Market Sentiment", data['label'])
                col3.metric("Polarity Score", data['avg_sentiment'])

                # Visualizing Headlines in a Table
                st.subheader("Key Sentiment Drivers")
                df = pd.DataFrame(data['headlines'])
                
                # Dynamic coloring for the sentiment scores
                def highlight_sentiment(val):
                    color = 'red' if val < 0 else 'green' if val > 0 else 'gray'
                    return f'background-color: {color}; color: white; font-weight: bold'

                st.dataframe(
                    df.style.applymap(highlight_sentiment, subset=['score']),
                    use_container_width=True
                )

        except Exception as e:
            st.error("Error: Ensure the Backend (app.py) is running on port 8000.")

st.sidebar.markdown("---")
st.sidebar.write("Built by Ediale Akhidenor | Data Science Portfolio")