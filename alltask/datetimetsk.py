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
plus=today.year+1
new_year=datetime.datetime(plus,1,1,0,0,0)
time_left=new_year-today
hours,reminder=divmod(time_left.seconds,3600)
reminder,seconds=divmod(reminder,60)

print(f'{time_left.days}days {hours}hours {reminder}minits {seconds}seconds to next New year')

#------------------------------------------------------------------------->
 #Accept two dates from the user and calculate how many days are between them.
user1=input("enter first date")
user2=input("enter second date")
converted=datetime.datetime.strptime(user1,"%d/%m/%Y")
converted1=datetime.datetime.strptime(user2,"%d/%m/%Y")
datee=converted-converted1

print("days",datee)


