import time
import requests

API_URL = "https://ema-signal-server.onrender.com/signal"

last_signal = ""

while True:
    try:
        res = requests.get(API_URL).json()

        signal = res["signal"]
        price = res["price"]

        if signal != last_signal:
            print("New Signal:", signal, price)

            if signal == "BUY":
                print("👉 Buy CE option")

            elif signal == "SELL":
                print("👉 Buy PE option")

            last_signal = signal

    except Exception as e:
        print("Error:", e)

    time.sleep(10)