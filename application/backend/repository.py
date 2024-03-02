from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import desc

import models, schemas


def get_weather_by_period(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weather).order_by(desc(models.Weather.created_at)).offset(skip).limit(limit).all()


def get_avg_weather_by_hour(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AvgWeatherHour).order_by(desc(models.AvgWeatherHour.created_at)).offset(skip).limit(limit).all()


def get_avg_weather_by_day(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AvgWeatherDay).order_by(desc(models.AvgWeatherDay.created_at)).offset(skip).limit(limit).all()


def create_weather(db: Session, weather: schemas.WeatherCreate):
    db_weather = models.Weather(temperature=weather.temperature, created_at=weather.created_at)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather


def create_avg_weather_hour(db: Session, weather: schemas.WeatherCreate):
    db_weather = models.AvgWeatherHour(temperature=weather.temperature, created_at=weather.created_at)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather


def create_avg_weather_day(db: Session, weather: schemas.WeatherCreate):
    db_weather = models.AvgWeatherDay(temperature=weather.temperature, created_at=weather.created_at)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

