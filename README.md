# stock_trader

A personal project where I'm building a stock trading bot in Python.

I first learned Python in 2023, but the files from back then are on a computer I can't get to anymore, so I started over this year. I'm building it by vibe coding: I describe what I want, run the code, read through it, and keep fixing things until I understand how it works.

## What it does now

- fetch_to_db.py: downloads 5 years of Samsung Electronics (005930.KS) prices with yfinance and saves them in a SQLite database
- strategy.py: reads the prices back with SQL and computes a 20-day and a 60-day moving average. The signal is "hold" when the 20-day is above the 60-day
- backtest.py: runs that signal over the past data and compares it to just buying and holding
- test_data.py: small check that the data download works

## First results

Over the 5 years of data, buy and hold returned about 320%. The moving average strategy returned about 194% after an assumed 0.2% cost per trade, over 25 trades. So the simple strategy did worse than holding. Samsung was in a strong uptrend, and the moving averages react late.

The 0.2% cost is my own rough assumption, and taxes are not included.

## What I want to do next

- Connect it to the Korea Investment & Securities (한국투자증권) API to get market data
- Place orders on their paper trading (모의투자) account first, not real money
- Try other stocks and time periods

## Running it

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python fetch_to_db.py
    python backtest.py
