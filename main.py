import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = "SBIN.NS"

sbi_data = yf.download(ticker,period="3y")

sbi_data["50_MA"] = sbi_data['Close'].rolling(window=50).mean()
sbi_data["200_MA"] = sbi_data['Close'].rolling(window=200).mean()
sbi_data["Daily_Return"] = sbi_data['Close'].pct_change() * 100
sbi_data = sbi_data.dropna()

plt.figure(figsize=(14,7))
plt.plot(sbi_data.index,sbi_data['Close'],label="Closing Price")
plt.plot(sbi_data.index,sbi_data['50_MA'],label="50 Days Moving Avg")
plt.plot(sbi_data.index,sbi_data['200_MA'],label="200 Days Moving Avg")
plt.legend()
plt.title("SBI Stock Trend Analysis")
plt.xlabel("Dates")
plt.ylabel("Price (INR)")

plt.show()
print(sbi_data.tail())