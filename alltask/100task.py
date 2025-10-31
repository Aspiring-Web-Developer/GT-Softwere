# function odd or even

# def find(number):
#     if number%2==0:
#         print("this number is even:",number)
#     else:
#         print("this number is even:",number)

# find(int(input("ENter the number")))

#----------------------------------------------------------------------------------->

#reverse number

# def reverse(num):
   
#     num1=0
#     while num>0:
#         digit=num%10
#         num1=num1*10+digit
#         num=num//10
#     print(num1)

# reverse(12345678)

#---------------------------------------------------------------------------->

# name="deepak"
# number="12345678"
# print(len(name))
# print(len(number))

#----------------------------------------------------------------------------->

# def palindrom(number):
#     og_number=number

#     sum_of_num=0
#     while number>0:
#         digit=number%10
#         sum_of_num=sum_of_num*10+digit
#         number=number//10
#     print(sum_of_num)

#     if og_number==sum_of_num:
#         print("palindrome")
#     else:
#         print("this is not palindrome")


# palindrom(121)

#------------------------------------------------------------------------------------->

# reverse string

# def reverse(str):
#     reverse_str="" 
#     for char in str:
#         reverse_str=char+reverse_str
#     print(reverse_str)
# reverse("deepak")

#----------------------------------------------------------------------------------->
#are of circlr
# import math

# def area_of(circle):
#     cal=math.pi*circle**2
#     print("the area of circle is :-",cal)

# area_of(float(input("Enter the number :-")))

#-------------------------------------------------------------------------------->

#squre of number

# def squre(num):
#      for i in range (0,num+1):
#         num1=i**2
#         print(num1,end="")
# squre(int(input("enter:")))

#----------------------------------------------------------------------------->

# string palindrome

# def rev_str(str):
#     string=str
#     empty=""
#     for i in str:
#         empty=i+empty
#     if empty==string:
#         print(empty,"This is palindrome")
#     else:
#         print(empty,"This is not palindrome")

# rev_str("mom")

#-------------------------------------------------------------------------------->

# factorial num

def factory(num):
      num1=1
      for i in range(1,num+1):
        num1=num1*i
        print(num1)
factory(5)