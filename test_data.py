import yfinance as yf
df = yf.download("005930.KS", period="1y", auto_adjust=True)
print(df.tail())