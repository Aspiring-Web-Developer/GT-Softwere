# #greaterthan

# a = int(input("Enter the number"))
# b= int(input("Enter the number"))
# c= int (input("Enter the number"))

# if a==b==c:
#     print("All number is equal")

# elif a>=b and b>=c:
#     print(a,"The number is greaterthan")

# elif b>=a and b>=c:
#      print(b,"this number is greaterthan")

# else:
#     print(c,"this number greater than")


# #divisbleboth

# num1=int(input("enter the number"))

# if num1%3==0 and num1%5==0:
#     print("the number is divisble both")

# elif num1%3==0:
#     print(num1,"this number divisible %3")

# elif num1%5==0:
#     print(num1,"this number divisible %5")

# else:
#     print(num1,"this number not divisible both")



# #number to days converter


# num7=int(input("type the number1-7"))

# if num7==1:
#     print('Sunady')

# elif num7==2:
#     print('monday')
# elif num7==3:
#     print('Tuesday')
# elif num7==4:
#     print("wednesday")
# elif num7==5:
#     print("thursday")
# elif num7==6:
#     print('friday')
# elif num7==7:
#     print("saturday")

# else:
#     print("invalid number")

# #login and password

# login1=input("enter the user name")
# password1=int(input("enter the password"))
# login="deepak"
# password=5787

# if login==login1 and password==password1:
#     print("login Sucessfully")

# else:
#      print("incorrect password or user name try again")

# #vote eligible

# votename=input("enter your name")
# age=int(input("enter your age"))

# if age > 0 and age <18:
#     print('not elg for vote')
# elif age>=18 and age<=75:
#     print('eligibile for vote')
# else:
#     print('senior citizens')

# #profit and loss

# cp=int(input("enter the cost price"))
# sp=int(input("enter the selling ptice"))

# if cp<=sp:
#     profit=sp-cp
#     print(profit,"profit")

# elif sp<=cp:
#     lose=cp-sp
#     print(lose,"loss")

# else:
#     print("invalid character")


# #calculate electricity


# bill=int(input("enter your units"))

# if bill<=100:
#     result=bill*5
#     print("your bill:-",result)
    
# elif bill<=200:
#       result=bill*7
#       print("your bill:-",result)
# else:
     
#       print("your bill:-",bill*10)


# #salary and taxes

# salary=int(input("enter your salary"))

# if salary<5000:
#     print("you have no taxes")
# elif salary>=5000 and salary<=10000:
#    tax_percent=10/100
#    salary2=tax_percent*salary
#    net_amnt=salary-salary2
#    print("your salary",salary,"your tax",tax_percent,"net amount",net_amnt)

# elif salary>=10001 and salary<=20000:
#     tax_percent=20/100
#     salary2=tax_percent*salary
#     net_amnt=salary-salary2
#     print("your salary",salary,"your tax",tax_percent,"net amount",net_amnt)

# else:
#     tax_percent=30/100
#     salary2=tax_percent*salary
#     net_amnt=salary-salary2
#     print("your salary",salary,"your tax",tax_percent,"net amount",net_amnt)
  



# #simple calculater

# calc=int(input("Enter the Number"))
# calc2=int(input("Enter another Number"))
# opreator=(input("Enter the Opreator +,-,*,/ "))

# if opreator=="+":
#     calc3=calc+calc2

#     print(calc3)

# elif opreator=="-":
#     calc3=calc-calc2

#     print(calc3)

# elif opreator=="*":
#     calc3=calc*calc2

#     print(calc3)

# elif opreator=="/":
#     calc3=calc/calc2

#     print(calc3)


# #collect the age
 
# age4=int(input("Enter Your age"))

# if age4<=12:
#     print("You're  child")

# elif age4>=13 and age4<=19:
#     print("you're Teenager")

# elif age4>=20 and age4<=59:
#     print("You are Adult")
# else:
#     print("you Are senior")


# #BMI calculation

height=float(input("Enter you Height"))
weight=float(input("Enter your Weight"))

bmi=weight/height**2

print("Ypur BMI is:",round(bmi,2))

if bmi<=18.5:
    print("You are under weight")

elif bmi>18.5 and bmi<=24.5:
    print("You are normel Weight")
elif bmi>24.5 and bmi<=29.5:
    print("You are over weight ")
else:
    print("you are obeses")


#Temprate Checker

temp=float(input("Enter The Temperature"))

if temp<15:
    print("your Weather is cold")

elif temp>15 and temp<=30:
    print("your weather is moderate")
else:
    print("your weather is hot")


    

for table in range(1,11):
    print(table,"x2=",table*2)