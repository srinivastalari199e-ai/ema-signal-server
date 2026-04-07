from fastapi import FastAPI
import requests

app = FastAPI()

# 👉 PASTE YOUR DETAILS HERE
TELEGRAM_TOKEN = "8530450406"
CHAT_ID = "8530450406"

data_store = {
    "index": "NIFTY",
    "signal": "WAIT",
    "price": 0
}

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/signal")
def get_signal():
    return data_store

@app.get("/update")
def update(index: str, signal: str, price: float):
    data_store["index"] = index
    data_store["signal"] = signal
    data_store["price"] = price

    # 🚨 SEND TELEGRAM ALERT
    msg = f"{index} {signal} @ {price}"
    send_telegram_message(msg)

    return {"status": "updated", "data": data_store}
