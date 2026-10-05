import sqlite3
import pandas as pd

COST = 0.002  # 매수 또는 매도 한 번당 0.2% 비용 (대략적인 가정)

conn = sqlite3.connect("prices.db")
df = pd.read_sql("SELECT date, close FROM prices ORDER BY date", conn)
conn.close()

df["ma20"] = df["close"].rolling(20).mean()
df["ma60"] = df["close"].rolling(60).mean()
df["signal"] = (df["ma20"] > df["ma60"]).astype(int)

df["daily_return"] = df["close"].pct_change()
df["position"] = df["signal"].shift(1)
df["trade"] = df["position"].diff().abs()
df["strategy_return"] = df["position"] * df["daily_return"] - df["trade"] * COST

buy_hold = (1 + df["daily_return"]).prod() - 1
strategy = (1 + df["strategy_return"].fillna(0)).prod() - 1

print(f"Buy and hold: {buy_hold:.1%}")
print(f"MA strategy (after costs): {strategy:.1%}")
print("Number of trades:", int(df["trade"].sum()))