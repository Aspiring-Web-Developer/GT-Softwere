# #list task dublicate value

# fruit=['apple','orange','pinnapple','apple','mango']
# unique=[]

# for i in fruit:
#     if i not in unique:
#         unique.append(i)
# print('orginal:',fruit)
# print('unique:',unique)
# print(len(unique))
# unique.sort()
# print(unique)

# #------------------------------------------------------------------------------------->
# #tuple

# a=(1,8,12,34,55,20)
# seat=int(input("enter the seat no"))




# if seat in a:
#     print(f"the{seat}seat is booked")
# else:
#     print(f"the {seat} seat not booked")

# count=0
# for reserve in range(1,11):
#      if reserve in a:
#          count+=1

# print(count,"seats are booked")

# convert=list(a)

# convert.append(78)
# print(convert)

# #---------------------------------------------------------------------------------------------->
# #set

# day1={'sita','ram','praveen','moorthi','bala'}
# day2={'sita','bala','nikil','laks','hussain'}

# print("present both days ",day1.intersection(day2))
# print("only on day",day1.difference(day2))
# print("all students",day1.union(day2))

# #---------------------------------------------------------------------------------------->
# #dic
# student = {
#     "Ram": {"math": 80, "science": 70},
#     "Sita": {"math": 90, "science": 95},
#     "Krishna": {"math": 60, "science": 50},

# }
# for name,marks in student.items():
#     total=sum(marks.values())

#     print(f"{name}:{total}")

# topper=None

# heighst=-1

# for name,marks in student.items():
#     if marks['science']>heighst:
#         heighst=marks['science']
#         topper=name
# print(topper,heighst)

# student["Ram"]['history']=88
# student["Sita"]['history']=78
# student["Krishna"]['history']=50

# print(student)

# for name,marks in student.items():
#     total=sum(marks.values())

#     print(f"{name}:{total}")

#------------------------------------------------------------------------------------->

#combo
# products = {"apple": 50, "banana": 20, "milk": 30, "bread": 40}
# cart = ["apple", "milk", "bread", "apple"]

# rebill=[]
# for i in cart:
#   if i not in rebill:
#     rebill.append(i)
# print(rebill)


# total=0
# for i in rebill:
#   total+=products[i]
#   print(f"{i}-{products[i]}")
#   print(total)
    
# if total>100:
#    net_amount=total-(total*0.10)
#    print(net_amount)
# else:
#   print("you have no discount")
  #------------------------------------------------------------------------------------------>

# ### 🔹 List Tasks
# 1. Maintain a shopping cart (list of items). Add, remove, and update items.
# 2. Given a list of daily temperatures for a week, find the highest, lowest, and average temperature.
# 3. From a list of student names, remove duplicates and sort alphabetically.
# 4. Store 10 bank transactions (positive for deposit, negative for withdrawal) and calculate final balance.
# 5. Given a list of words, find the longest and shortest word.
#----------------------------------------------------------------------------------------->

# cart=['apple','orange','grapes','pinapple']
# cart.append('watermelon')
# print(cart)
# cart.remove('pinapple')
# print(cart)
# cart.insert(1,'bomogradient')
# print(cart)
#----------------------------------------------------------------------------------------->


temprature=[]

for i in range(7):
    temp= float(input(f"enter the temprature{i+1}"))
    temprature.append(temp)
  

highst=max(temprature)
lowest=min(temprature)
average=sum(temprature)/len(temprature)

print("highst temprature",highst)
print("lowest temprature",lowest)
print("average temprature",average ,(round,2))

#---------------------------------------------------------------------------------------->

# student=['shanmugam','laks','lakshmanan','laks','kaviya','malar','shanmugam']

# student1=[]

# for i in student:
#     if i not in student1:
#         student1.append(i)
# print(student1)

# student1.sort()
# print(student1)

#----------------------------------------------------------------------------------------->

# transaction=[2000,8000,4300,9000,5500,-300,-200,-8000,-4500,-5000]


# balance=0
# for i in transaction:
#      balance+=i

# print(balance)
 

    

# print(total1,total2)

# net_amount=total1+total2

# print("your bank balance",net_amount)


# dublicates

dublicates=[10,30,60,30,70,80,60,10]

og_numbers=[]

for i in dublicates:
    if i not in og_numbers:
        og_numbers.append(i)
print(og_numbers)