# Step 1: Import necessary packages
import streamlit as st
import yfinance as yf
import pandas as pd
import io
import base64

# Step 2: Define a function to get and filter stock data
def get_and_filter_stocks(min_price=20, max_price=180, min_beta=2.0):
    # Note: This step assumes you have a predefined list of US stock symbols
    stocks = ["AAPL", "MSFT", "GOOGL"]  # example list, replace with your own list
    filtered_stocks = []

    for stock in stocks:
        ticker = yf.Ticker(stock)
        info = ticker.info

        # Checking if beta and current price fall within specified range
        if info['beta'] >= min_beta and min_price <= info['regularMarketPrice'] <= max_price:
            filtered_stocks.append(info)

    return pd.DataFrame(filtered_stocks)

# Step 3: Streamlit app
st.title("Filtered US Stocks")

# User inputs
min_price = st.sidebar.number_input("Minimum Price", 20, 1000, 20)
max_price = st.sidebar.number_input("Maximum Price", 20, 1000, 180)
min_beta = st.sidebar.number_input("Minimum Beta", 1.0, 3.0, 2.0)

# Get and filter stocks
df = get_and_filter_stocks(min_price, max_price, min_beta)

# Display data
st.write(df)

# Download data as excel
if st.button('Download Data'):
    towrite = io.BytesIO()
    downloaded_file = df.to_excel(towrite, index=False, header=True)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.getvalue()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="filtered_stocks.xlsx">Download Excel File</a>'
    st.markdown(href, unsafe_allow_html=True)
