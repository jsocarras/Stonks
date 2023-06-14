# Step 1: Import necessary packages
import streamlit as st
import yfinance as yf
import pandas as pd

# Step 2: Define a function to get and filter stock data
def get_and_filter_stocks(companies, min_price=20, max_price=180, max_beta=2.0):
    filtered_stocks = []
    fields_of_interest = ['shortName', 'symbol', 'industry', 'sector', 'fullTimeEmployees', 'regularMarketPrice', 'beta']

    for company in companies:
        ticker = yf.Ticker(company)
        info = ticker.info

        # Checking if beta and current price exist and fall within specified range
        if 'beta' in info and 'regularMarketPrice' in info:
            if info['beta'] <= max_beta and min_price <= info['regularMarketPrice'] <= max_price:
                filtered_stock = {field: info.get(field, None) for field in fields_of_interest}
                filtered_stocks.append(filtered_stock)

    return pd.DataFrame(filtered_stocks)

# Step 3: Streamlit app
st.title("Filtered Fortune 50 US Stocks")

# User inputs
min_price = st.sidebar.number_input("Minimum Price", 20, 1000, 20)
max_price = st.sidebar.number_input("Maximum Price", 20, 1000, 180)
max_beta = st.sidebar.number_input("Maximum Beta", 1.0, 3.0, 2.0)

# Fortune 50 company stock symbols
companies = ["WMT", "BRK.A", "AAPL", "XOM", "CVX", "JNJ", "WBA", "AMZN", "T", "GM",
             "F", "HCA", "CVS", "MCK", "UNH", "ABC", "CI", "TGT", "DAL", "HPQ",
             "COST", "KR", "ACN", "SLB", "AIG", "PSX", "TSN", "JPM", "LMT", "MSFT",
             "MAR", "C", "BAC", "KO", "INTC", "AAL", "DVA", "SYF", "OXY", "COP",
             "IBM", "MET", "CAT", "SO", "WFC", "BA", "GS", "GE", "MRK", "GM"]

# Get and filter stocks
df = get_and_filter_stocks(companies, min_price, max_price, max_beta)

company_to_examine = st.sidebar.selectbox("Select a Company to Examine", companies)
if company_to_examine:
    ticker = yf.Ticker(company_to_examine)
    info = ticker.info
    df_info = pd.DataFrame.from_dict(info, orient='index').reset_index()
    df_info.columns = ['Attribute', 'Value']
    st.table(df_info)
    
# Display data
st.write(df)
