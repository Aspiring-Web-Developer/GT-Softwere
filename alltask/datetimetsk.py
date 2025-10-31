import datetime
today=datetime.datetime.now()

# current= datetime.datetime.strptime("20-11-2025 13:15:45","%d-%m-%Y %H:%M:%S")

print(today)
print(today.strftime("%d-%m-%Y %H:%M:%S"))

#--------------------------------------------------------------------------------->

# Userdb=(input("Enter Your Date Of Birth"))
# convert=datetime.datetime.strptime(Userdb,"%d/%m/%Y")
# year=today.year
# total=year-convert.year
# print("your age is:",total)

#-----------------------------------------------------------------------------
# plus=today.year+1
# new_year=datetime.datetime(plus,1,1,0,0,0)
# time_left=new_year-today
# hours,reminder=divmod(time_left.seconds,3600)
# reminder,seconds=divmod(reminder,60)

# print(f'{time_left.days}days {hours}hours {reminder}minits {seconds}seconds to next New year')

#------------------------------------------------------------------------->
 #Accept two dates from the user and calculate how many days are between them.
# user1=input("enter first date")
# user2=input("enter second date")
# converted=datetime.datetime.strptime(user1,"%d/%m/%Y")
# converted1=datetime.datetime.strptime(user2,"%d/%m/%Y")
# datee=converted1-converted

# print("days",datee)

#----------------------------------------------------------------------------->

 #Ask the user for a date (e.g., `2025-08-15`) and print the corresponding weekday (e.g., `Friday`).

# one=input("enter the date")
# converted1=datetime.datetime.strptime(one,"%d/%m/%Y")
# converted2=datetime.datetime.strftime(converted1,"%A")
# print(converted2)

#------------------------------------------------------------------------------->

#* Log current date and time whenever an event (like a print statement) happens.
# def timegame(message):
#     today=datetime.datetime.now()

#     timstame=today.strftime("%d/%m/Y %H:%M:%S")

#     print(f'{timstame},{message}')

# timegame("starting")
# timegame("click")
# timegame("end")

#----------------------------------------------------------------------------->

# Convert a date string like `"2025-06-10"` into a more readable format like `"10th June 2025"`.

# date="25/10/2025"

# datec=datetime.datetime.strptime(date,"%d/%m/%Y")
# dat=datec.day
# month=datetime.datetime.strftime(datec,"%B")

# year=datec.year

# print(f'{dat}th {month}{year}')

#------------------------------------------------------------------------------------->

# bir_list=["10/04/2002","24/08/2005","14/10/2003","05/08/2003","31/10/2025"]

# for date in bir_list:

#     conv=datetime.datetime.strptime(date,"%d/%m/%Y")
#     if today.month==conv.month:
#         print("This Month Birthday Lists", date)

#-------------------------------------------------------------------->

# user=input("enter time")
# user2=input("enter another time")

# conv=datetime.datetime.strptime(user,"%H:%M:%S")
# conv1=datetime.datetime.strptime(user2,"%H:%M:%S")
# # cal=conv.hour,conv.minute
# # cal2=conv1.hour,conv.minute
# # total=cal-cal2
# print(conv-conv1)
#----------------------------------------------------------------->

#Take a given date and add or subtract a specific number of days and show the result.
date="10/10/2025"
cov=datetime.datetime.strptime(date,"%d/%m/%Y")

future = cov+ datetime.timedelta(days=int(input("enter date")))
print(future)



