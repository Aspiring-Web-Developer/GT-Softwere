

num1=int(input("Enter the Number"))
num2=int(input("Enter another Number"))
opreator=(input("Enter the Opreator +,-,*,/,% "))

if opreator=="+":
    result=num1+num2

    print(result)

elif opreator=="-":
    result=num1-num2

    print(result)

elif opreator=="*":
    result=num1*num2

    print(result)

elif opreator=="/":
    result=num1/num2

    print(result)
else:
    print("invalid charcter")