# name=input("enter the name")

# for i in name:
#       if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             continue
          
#       print(i)

# for i in range(2,51):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#           is_prime=False
#           break
#     if is_prime:
#        print(i)

# name=input("Enter Name")
# vows=0
# cons=0

# for i in name:
#    print(i)
#    if i=="a" or i=="e" or  i=="i" or i=="o" or i=="u":
#       vows+=1
#    else:
#       cons+=1
# print(vows)
# print(cons)
   
for i in range(1,11):
    print("-"*25)
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        
      