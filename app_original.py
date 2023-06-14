import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from openpyxl import Workbook

# Assuming you have a list of tickers
tickers = ["AAPL", "GOOG", "MSFT", "AMZN"]

def get_filtered_stocks(tickers):
    filtered_stocks = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        if 2 <= stock.info['beta'] <= 2.5 and 20 <= stock.info['regularMarketPrice'] <= 180:
            filtered_stocks.append(stock.info)
    return filtered_stocks

def write_to_excel(stocks):
    df = pd.DataFrame(stocks)
    df.to_excel('filtered_stocks.xlsx')

def main():
    stocks = get_filtered_stocks(tickers)
    write_to_excel(stocks)
    st.write('Filtered stocks have been written to filtered_stocks.xlsx')

if __name__ == "__main__":
    main()
