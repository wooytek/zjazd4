import random
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
import uvicorn

app = FastAPI()

DB_URL = "mysql+mysqlconnector://root:@localhost/qwer"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100))
    temperature = Column(Float)
    humidity = Column(Float)
    date = Column(DateTime, default=datetime.now)


Base.metadata.create_all(bind=engine)

@app.get("/weather/{city_name}")
def get_city(city_name: str):
    db = SessionLocal()
    city_temp = db.query(Weather).filter(Weather.city == city_name).first()
    db.close()

    if city_temp:
        return {
            "city": Weather.city,
            "temperature": Weather.temperature,
            "humidity": Weather.humidity,
            "date": str(Weather.date)
        }
    return {"error": "Post not found"}

# @app.get("/weather")
# def get_all_cities():
#     db = SessionLocal()
#     cities = db.query(Weather).all()
#     db.close()
#     # response = []
#     # for post in posts:
#     #     j = {"id": post.id, "author": post.author, "content": post.content, "date": str(post.date)}
#     #     response.append(j)
#
#     response = [{"id": city.city, "author": city.temperature, "content": city.humidity, "date": str(city.date)} for city in cities]
#
#     return response



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)