import logging
import datetime
import helpers


import repository
from schemas import WeatherCreate
from db import SessionLocal
import consts


def realtime_log(temp):
    logging.basicConfig(level=logging.INFO, filename=consts.REALTIME_LOG_PATH,
                    format="%(asctime)s | %(message)s")
    logging.info(temp)


    repository.create_weather(
        SessionLocal(),
        WeatherCreate(temperature=temp, created_at=datetime.datetime.now())
    )


def avg_hour_log():
    count = 0
    temp_sum = 0
    date_now = datetime.datetime.now()
    logging.basicConfig(level=logging.INFO, filename=consts.AVG_HOUR_LOG_PATH,
                    format="%(asctime)s | %(message)s")

    with open(consts.REALTIME_LOG_PATH) as f:
        lines = f.readlines()
        for line in lines:
            parsed_line = line.split(' | ')
            date_from_file = datetime.datetime.strptime(parsed_line[0], '%Y-%m-%d %H:%M:%S,%f')

            if helpers.equal_hour_of_day(date_now, date_from_file):
                count += 1 
                temp_sum += int(parsed_line[1][0:len(parsed_line[1])-1])
        
    avg = helpers.write_avg_log(temp_sum, count)

    repository.create_avg_weather_hour(
        SessionLocal(),
        WeatherCreate(temperature=avg, created_at=datetime.datetime.now())
    )


def avg_day_log():
    count = 0
    temp_sum = 0
    date_now = datetime.datetime.now()
    logging.basicConfig(level=logging.INFO, filename=consts.AVG_DAY_LOG_PATH,
                    format="%(asctime)s | %(message)s")

    with open(consts.AVG_HOUR_LOG_PATH) as f:
        lines = f.readlines()
        for line in lines:
            parsed_line = line.split(' | ')
            date_from_file = datetime.datetime.strptime(parsed_line[0], '%Y-%m-%d %H:%M:%S,%f')

            if helpers.equal_day(date_now, date_from_file):
                count += 1 
                temp_sum += int(parsed_line[1][0:len(parsed_line[1])-1])
        
    avg = helpers.write_avg_log(temp_sum, count)

    repository.create_avg_weather_day(
        SessionLocal(),
        WeatherCreate(temperature=avg, created_at=datetime.datetime.now())
    )


def clear_realtime_log():
    date_now = datetime.datetime.now()
    with open(consts.REALTIME_LOG_PATH, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            parsed_line = line.split(' | ')
            date_from_file = datetime.datetime.strptime(parsed_line[0], '%Y-%m-%d %H:%M:%S,%f')
            if not helpers.older_than_day(date_now, date_from_file):
                f.write(line)
            f.truncate()


def clear_avg_hour_log():
    date_now = datetime.datetime.now()
    with open(consts.AVG_HOUR_LOG_PATH, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            parsed_line = line.split(' | ')
            date_from_file = datetime.datetime.strptime(parsed_line[0], '%Y-%m-%d %H:%M:%S,%f')
            if not helpers.older_than_month(date_now, date_from_file):
                f.write(line)
            f.truncate()


def clear_avg_day_log():
    date_now = datetime.datetime.now()
    with open(consts.AVG_DAY_LOG_PATH, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            parsed_line = line.split(' | ')
            date_from_file = datetime.datetime.strptime(parsed_line[0], '%Y-%m-%d %H:%M:%S,%f')
            if not helpers.older_than_year(date_now, date_from_file):
                f.write(line)
            f.truncate()