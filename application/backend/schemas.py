from pydantic import BaseModel
from datetime import datetime



class WeatherBase(BaseModel):
    temperature: int
    created_at: datetime


class WeatherCreate(WeatherBase):
    pass


class Weather(WeatherBase):
    id: int

    class Config:
        orm_mode = True

