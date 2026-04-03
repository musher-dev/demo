from fastapi import FastAPI, HTTPException

app = FastAPI()

MOCK_DATA = {
    "london": {"temp_c": 12, "condition": "Cloudy"},
    "tokyo": {"temp_c": 22, "condition": "Sunny"},
    "new-york": {"temp_c": 18, "condition": "Partly cloudy"},
}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/weather/{city}")
def get_weather(city: str):
    key = city.lower().strip()
    if key not in MOCK_DATA:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found")
    return {"city": city, **MOCK_DATA[key]}
