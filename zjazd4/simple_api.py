from datetime import datetime
from fastapi.responses import HTMLResponse

from fastapi import FastAPI, Response
from zjazd4 import uvicorn1

app = FastAPI()

@app.get("/")
def hello():
    return { "message": "Witaj świecie!"}

@app.get("/weather/simple")
def get_weather_simple1():
    return {
        "temperature": 36.6,
        "humidity": 70,
        "timestamp": datetime.now()
    }

@app.get("/xml")
def get_xml():
    title = "Witaj w moim api"
    xml_data = f"""<?xml version="1.0"?>
    <message>
        <title>{title}</title>
        <h1>Witaj Merito!</h1>
        <p>BigData</p>
    </message>
    """
    return Response(content=xml_data, media_type="application/xml")

@app.get("/json")
def get_json():
    return {
        "title": "Witaj w moim api",
        "h1": "Witaj Merito!",
        "p": "BigData"
    }

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return """<!DOCTYPE html>
<html>
    <head>
        <title>Witaj w moim api</title>
    </head>
    <body>
        <h1>Witaj Merito!</h1>
        <p>BigData
    </body>
</html>
    """




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)