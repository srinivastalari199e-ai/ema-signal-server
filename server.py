from fastapi import FastAPI
import yfinance as yf
import pandas as pd
import threading
import time

app = FastAPI()

latest_signal = {
    "index": "NIFTY",
    "signal": "WAIT",
    "price": 0
}

def calculate_signal():
    global latest_signal

    while True:
        try:
            data = yf.download("^NSEI", interval="15m", period="2d")

            data['EMA7'] = data['Close'].ewm(span=7).mean()

            last = data.iloc[-1]

            price = float(last['Close'])
            ema = float(last['EMA7'])

            if price > ema:
                signal = "BUY"
            else:
                signal = "SELL"

            latest_signal = {
                "index": "NIFTY",
                "signal": signal,
                "price": price
            }

            print("Updated:", latest_signal)

        except Exception as e:
            print("Error:", e)

        time.sleep(60)  # every 1 min


@app.on_event("startup")
def start_thread():
    thread = threading.Thread(target=calculate_signal)
    thread.start()


@app.get("/")
def home():
    return {"status": "running"}


@app.get("/signal")
def get_signal():
    return latest_signal
