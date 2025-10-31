# reverse loop

# for i in range(30,2,3):
#     print(i)
    

# while loop
# n=5
# fact=1
# for i in range(n,0,-1):
#     fact*=i
#     print(i)
#     if(i!=1):
        
#         print("give num of",i,"is",fact)
   

# print("fact of",n,"is",fact)


# sumdig=0
# while fact!=0:
#         sumdig+=fact%10
#         fact=fact//10
#         print(sumdig)



# while loop 2

# num=153
# sumdig=0
# while num!=0:
     
#       sumdig+=num%10
#       num=num//10

#       onam=num**3
#       print(num,onam)

#while loop3
num=int(input("enter any number"))
temp=num


sum_digit=0

while temp>0:
     digit=temp%10
     sum_digit+=digit**3
     temp//=10

if (sum_digit==num):
     print("This is amstrong number")
else:
     print("this is not amstrong")
     



