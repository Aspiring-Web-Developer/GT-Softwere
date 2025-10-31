#odd or even

find=int(input("put the any number"))

if find %2==0:
    print("The Number is even")

else:
    print("The Number is odd")

    
#positive negative zero

which=int(input("type the number"))

if which>0:
    print("Positve")

else:
    print("negative")


#print large num

num1=int(input("type the 1st number"))
num2=int(input("type the 2nd number"))
 
if num1>num2:
    print(num1,"this number is large one")

else:
    print(num2,"this number is large one")


#the number is divisible 5%

divisble=int(input("Type the any number" ))

if divisble %5==0:
    print(divisble,"This number divisble 5")
else:
    print(divisble,"this number not divisble 5")


#leap year

year=int(input("Enter the Year"))

if year %4==0:
    print(year,"This is Leap Year")

else:
     print(year,"This is not leap Year")


#eligible to vote

vote=int(input("Enter your Age"))

if vote>=18:
    print("You are eligible to vote")

else:
    print("you are not eligible to vote")


#add and substraction

value1=int(input("Enter the 1st number"))
value2=int(input("Enter the 2nd number "))
opretor=input( "enter the any opretor  (+or-)")

if opretor=="+":
   result=value1+value2
   print(result)

else:
    result=value1-value2
    print(result)


#profit and loss

cp=int(input("enter the cost price"))
sp=int(input("enter the selling price"))

if sp>cp:
    profit=sp-cp
    print(profit,"profit")
else:
    print("Loss")
