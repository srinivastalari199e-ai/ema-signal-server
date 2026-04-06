from fastapi import FastAPI, Request

app = FastAPI()

latest_signal = {
    "index": "NIFTY",
    "signal": "WAIT",
    "price": 0
}

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/signal")
def get_signal():
    return latest_signal

@app.post("/update")
async def update_signal(request: Request):
    global latest_signal
    data = await request.json()
    latest_signal = data
    print("Received:", data)  # helps debug
    return {"status": "updated"}
