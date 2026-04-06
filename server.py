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

       last_close = data['Close'].iloc[-1]
last_ema = data['EMA7'].iloc[-1]

price = float(last_close)
ema = float(last_ema)

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
