from fastapi import FastAPI
import yfinance as yf
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}


@app.get("/signal")
def get_signal():
    try:
        data = yf.download("^NSEI", interval="15m", period="2d")

        if data.empty:
            return {"error": "No market data"}

        data['EMA7'] = data['Close'].ewm(span=7).mean()

        last = data.iloc[-1]

        price = float(last['Close'])
        ema = float(last['EMA7'])

        if price > ema:
            signal = "BUY"
        else:
            signal = "SELL"

        return {
            "index": "NIFTY",
            "signal": signal,
            "price": price
        }

    except Exception as e:
        return {"error": str(e)}
