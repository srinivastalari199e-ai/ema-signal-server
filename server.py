from fastapi import FastAPI

app = FastAPI()

latest_signal = {
    "index": "NIFTY",
    "signal": "WAIT",
    "price": 0
}

@app.get("/")
def home():
    return {"status": "running"}

# ✅ Always return latest signal (NO external API)
@app.get("/signal")
def get_signal():
    return latest_signal

# ✅ Update signal (THIS is your main entry)
@app.get("/update")
def update_signal(index: str, signal: str, price: float):
    global latest_signal

    latest_signal = {
        "index": index,
        "signal": signal,
        "price": price
    }

    return {"status": "updated", "data": latest_signal}
