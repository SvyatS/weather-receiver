import logging
from datetime import timedelta




def equal_hour_of_day(date_now, date_from_file):
    return (date_now.hour == date_from_file.hour 
       and date_now.day == date_from_file.day
       and date_now.month == date_from_file.month
       and date_now.year == date_from_file.year)


def equal_day(date_now, date_from_file):
    return (date_now.day == date_from_file.day
       and date_now.month == date_from_file.month
       and date_now.year == date_from_file.year)


def write_avg_log(temp_sum, count):
    if temp_sum == 0:
        logging.info(0)
        return 0
    else:
        logging.info(int(temp_sum / count))
        return int(temp_sum / count)

    


def older_than_day(date_now, file_date):
    return date_now - timedelta(days=1) >= file_date


def older_than_month(date_now, file_date):
    return date_now - timedelta(days=30) >= file_date


def older_than_year(date_now, file_date):
    return date_now - timedelta(days=365) >= file_date