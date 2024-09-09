import random as rm
import time as tm
def get_random_date(start_date,end_date):
    print("Date between these dates is : ")
    random_generator=rm.random()
    date_format="%m/%d/%Y"
    start_time=tm.mktime(tm.strptime(start_date,date_format))
    end_time=tm.mktime(tm.strptime(end_date,date_format))
    random_time=start_time+random_generator*(end_time-start_time)
    random_date=tm.strftime(date_format,tm.localtime(random_time))
    return random_date
print("Random date is : ",get_random_date("01/01/2013","12/31/2024"))
