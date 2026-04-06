from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

# Store latest signal
latest_signal = {
    "index": "NIFTY",
    "signal": "WAIT",
    "price": 0
}

# ✅ Root check
@app.get("/")
def home():
    return {"status": "running"}

# ✅ Get signal
@app.get("/signal")
def get_signal():
    global latest_signal

    try:
        # Fetch NIFTY data
        symbol = "^NSEI"
        data = yf.download(symbol, period="1d", interval="5m")

        if data is None or data.empty:
            return {"error": "No market data"}

        # Get latest price
        last_close = float(data['Close'].iloc[-1])

        # Simple logic (you can upgrade later)
        if last_close > 0:
            signal = "BUY"
        else:
            signal = "SELL"

        latest_signal = {
            "index": "NIFTY",
            "signal": signal,
            "price": last_close
        }

        return latest_signal

    except Exception as e:
        return {"error": str(e)}

# ✅ Manual update (for testing / webhook)
@app.get("/update")
def update_signal(index: str, signal: str, price: float):
    global latest_signal

    latest_signal = {
        "index": index,
        "signal": signal,
        "price": price
    }

    return {"status": "updated"}
