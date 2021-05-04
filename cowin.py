import os
import schedule
import time
from cowin_api import CoWinAPI
from datetime import datetime

district_id = '776'  # surat corporation
date = '04-05-2021'  # Optional. Takes today's date by default
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def get_availability():
    cowin = CoWinAPI()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
    for i in available_centers['centers']:
        for x in i['sessions']:
            if x['available_capacity'] > 0:
                print(i['name'], "\t", i['pincode'], "\t", x['available_capacity'], current_time)


schedule.every(20).seconds.do(get_availability)
schedule.every(20).minutes.do(screen_clear)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
