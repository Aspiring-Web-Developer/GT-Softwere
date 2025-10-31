#odd Number

# for odd in range(1001,1020,2):
#     print(odd)

# for odd1 in range(1000,1020):
#   if odd1 %2 !=0:
#       print(odd1)


#squre of numbers

# for num in range(1,5):
#     squre=num**2
#     print(f"Squre of{num}is of{squre}")



#cube even num

# for num in range(1,11):

#    if num %2==0:
#     squre=num**3
#     print(f"cube of{num}is of{squre}")


#addition table
# num=int(input("Enter the range num"))

# for i in range(1,11):
#     print(f"{num}+{i}={num+i}")

# for i in range(1,10):
#     print(5*i)



sum=0

for i in range(1,5,):
    # sum=sum+i  #cart example
    sum+=i
    # print(sum)

print('final answer',sum)



# # get sum of square of numbrs
# # get sum of even number from 1 to 10

# # find factorial  5! 1*2*#..5




# # sum_of_squre=0
# # for i in range(1,10):
# #     sum_of_squre+=i**2
# #     print("sum of squre of ",i,"is on",sum_of_squre)

# sum_of_squre=0
# for i in range(0,11,2):
#     sum_of_squre=i**2
#     print("sum of squre of ",i,"is on",sum_of_squre)

num=5
fact=1
for i in range(1,num+1):
    fact*=i
    print("default number",num,"multiplication number",fact)


for i in range(10,0,-1):
    print(i)


passwrd='12345'

# userpass=input('enter yr passwrd: ')

# while passwrd!=userpass:
#   if(passwrd!=userpass):
#      print('your password is incorrect')
#      userpass=input('enter yr passwrd: ')

#   else:
#      break
  

num=124
sumdig=0

while num!=0:
   sumdig+=num%10
   num=num//10
   print(f"num, {num}")
   print(f"sum {sumdig}")


print('Sum of digitit is ',sumdig)
   
