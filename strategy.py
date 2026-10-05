import sqlite3
import pandas as pd

conn = sqlite3.connect("prices.db")
df = pd.read_sql("SELECT date, close FROM prices ORDER BY date", conn)
conn.close()

df["ma20"] = df["close"].rolling(20).mean()
df["ma60"] = df["close"].rolling(60).mean()
df["signal"] = (df["ma20"] > df["ma60"]).astype(int)

print(df.tail(10))
print("Days holding:", df["signal"].sum(), "of", len(df))
