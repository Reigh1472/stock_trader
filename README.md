# stock_trader

A personal project where I'm building a stock trading bot in Python.

I first learned Python in 2023, but the files from back then are on a computer I can't get to anymore, so I started over this year. I'm building it by vibe coding: I describe what I want, run the code, read through it, and keep fixing things until I actually understand how it works. It's mostly a way to get back into Python and learn how a trading system fits together.

## Where it's at

Right now it just downloads some sample stock data to check that my setup works (test_data.py). Nothing more yet.

## What I want to do next

- Connect it to the Korea Investment & Securities (한국투자증권) API to get real market data
- Clean up the data
- Try a couple of simple trading strategies on it

## Running it

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python test_data.py
