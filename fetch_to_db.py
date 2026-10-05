import sqlite3
import yfinance as yf

df = yf.download("005930.KS", period="5y", auto_adjust=True)
df.columns = df.columns.get_level_values(0)
df = df.reset_index()
df.columns = [c.lower() for c in df.columns]

conn = sqlite3.connect("prices.db")
df.to_sql("prices", conn, if_exists="replace", index=False)

for row in conn.execute("SELECT COUNT(*), MIN(date), MAX(date) FROM prices"):
    print(row)
conn.close()
