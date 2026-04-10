import yfinance as yf
import pandas as pd

ticker = "SBIN.NS"

sbi_data = yf.download(ticker,period="1y")

sbi_data["50_MA"] = sbi_data['Close'].rolling(window=50).mean()
sbi_data["200_MA"] = sbi_data['Close'].rolling(window=200).mean()
sbi_data["Daily_Return"] = sbi_data['Close'].pct_change() * 100


sbi_data.dropna()
print(sbi_data.tail())