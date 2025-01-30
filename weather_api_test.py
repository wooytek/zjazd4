from datetime import datetime
import random
from fastapi import FastAPI, Response, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return { "message": "Witaj świecie!"}
@app.get("/weather/{city}")
def get_weather_simple(city: str):
    return {
        "city": city,
        "temperature": random.uniform(-15,45),
        "humidity": random.uniform(40,80),
        "timestamp": datetime.now()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)