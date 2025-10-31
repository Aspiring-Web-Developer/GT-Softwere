date = "30/10/2025"

import datetime

today = datetime.datetime.now()

print(today.time())

today_date = datetime.date.today()
print(today_date)

doj = datetime.date(2024,11,23)
time = datetime.time(11,23,23)
print(doj)

print(today_date-doj)

dob = datetime.datetime(2000,8,12,10,30)
print(dob)
print(today-dob)

future = today + datetime.timedelta(days=10)

print(future)
past = today- datetime.timedelta(weeks=12,days=10,hours=4)
print(past)

print(today.weekday())
print(today.isocalendar())

print(today.timestamp())

print(today.strftime("%d/%m/%Y"))
doj = datetime.datetime.strptime("2025-1-23 12:45:56","%Y-%m-%d %H:%M:%S")

print(doj)