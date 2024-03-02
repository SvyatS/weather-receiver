from sqlalchemy import Column, Integer, DateTime
import datetime

from db import Base


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)
    temperature = Column(Integer, index=True)
    created_at = Column(DateTime, index=True)


class AvgWeatherHour(Base):
    __tablename__ = "avg_weather_hour"

    id = Column(Integer, primary_key=True)
    temperature = Column(Integer, index=True)
    created_at = Column(DateTime, index=True)


class AvgWeatherDay(Base):
    __tablename__ = "avg_weather_day"

    id = Column(Integer, primary_key=True)
    temperature = Column(Integer, index=True)
    created_at = Column(DateTime, index=True)