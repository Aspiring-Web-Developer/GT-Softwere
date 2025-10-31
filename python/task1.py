#username and password

# username1="deepak"
# password2=7373155

# username=input("Enter your user name")
# password=int(input("Enter your password"))

# for i in range(1,4):
#     if password2!=password:
#         print(i,"your password is incorrect")
#         password=int(input("Enter your password"))
     
#     else:
#         break

# print("login successful")

# num=int(input("enter any number"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
#     print("default number",i,"multiplication number",fact)



#prime Number
# num=int(input("Enter any number"))

# for i in range(2,101):
#     digit=num%i
#     if (num%i==0):
#         print(digit,"not prime")
#     elif(num%i!=0):
#         print(digit,"it is prime number")
#     else:
#         break


#
# for i in range(1,101):
#     if (i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz",end="")
#     else:
#         print(i)

# triangle
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        
        print("*",end="")
    print()

num=5

for i in range(1,num+1):
    print()
    for j in range(num-i):
        print(' ',end="")
    for k in range(i*2-1):
        print("*",end="")

# num=10
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# num=5
# for i in range(num,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# num=4
# row=1
# for i in range(1,num+1):
#    for j in range(1,i+1):
#      print(row,end="")
#      row += 1
#    print()


#parlindrome


# word=input("Enter the name")


# if word==word[::-1]:
#      print("This is parlindrome")
# else:
#      print("this is not")


#gcd

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# gcd=1
# for i in range(1,min(num1,num2)+1):
#     if num1%i==0 and num2%i==0:
#      gcd=i
#     print("GCD of",num1,"and",num2,"the:",gcd)