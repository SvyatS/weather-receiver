from fastapi import APIRouter, Depends
from datetime import datetime
from sqlalchemy.orm import Session

import repository, models, schemas
from db import SessionLocal




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/api/v1", dependencies=[Depends(get_db)])


@router.get("/weather/", response_model=list[schemas.Weather])
def read_weather(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    weathers = repository.get_weather_by_period(db, skip=skip, limit=limit)
    return weathers


@router.get("/avg-weather-by-hour/", response_model=list[schemas.Weather])
def read_weather(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    weathers = repository.get_avg_weather_by_hour(db, skip=skip, limit=limit)
    return weathers


@router.get("/avg-weather-by-day/", response_model=list[schemas.Weather])
def read_weather(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    weathers = repository.get_avg_weather_by_day(db, skip=skip, limit=limit)
    return weathers