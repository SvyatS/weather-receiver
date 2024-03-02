import schedule
import time

import logs




schedule.every().hour.do(logs.avg_hour_log)
schedule.every().day.at("00:00").do(logs.avg_day_log)

schedule.every(5).minutes.do(logs.clear_realtime_log)
schedule.every().hour.do(logs.clear_avg_hour_log)
schedule.every().day.at("00:01").do(logs.clear_avg_day_log)

while True:
    schedule.run_pending()
    time.sleep(60)



