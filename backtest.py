import sqlite3
import pandas as pd

conn = sqlite3.connect("prices.db")
df = pd.read_sql("SELECT date, close FROM prices ORDER BY date", conn)
conn.close()

df["ma20"] = df["close"].rolling(20).mean()
df["ma60"] = df["close"].rolling(60).mean()
df["signal"] = (df["ma20"] > df["ma60"]).astype(int)

df["daily_return"] = df["close"].pct_change()
df["strategy_return"] = df["signal"].shift(1) * df["daily_return"]

buy_hold = (1 + df["daily_return"]).prod() - 1
strategy = (1 + df["strategy_return"].fillna(0)).prod() - 1

print(f"Buy and hold: {buy_hold:.1%}")
print(f"MA strategy:  {strategy:.1%}")
