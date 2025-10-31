# numb=[10,20,40]

# print(numb)

# print(len(numb))


# #adding values
# numb.append(50)#it will add element in last 
# print(numb)

# numb.extend([60,70,80]) #it will more values in end
# print(numb)

# numb.insert(2,30) #it will add at particular index
# print(numb)


# fruits = ["apple","jkjls", "banana", "orange", "mango", "grapes", "pineapple"]
# print(fruits)
# print(len(fruits))

# print(fruits[5])
# # print(fruits[6])

# #removing values
# print(fruits)
# fruits.pop()#it will remove last element (if u mention parameter as empty)
# print(fruits)

# fruits.pop(3)#it will remove specified  element in that index (if u mention parameter as empty)
# print(fruits)

# fruits.remove('grapes')
# print(fruits)

# fruits.clear()
# print(fruits)

# a=[1,4,5,6,9,1,2,4,5]
# # a.sort()#ascending
# # print(a)

# a.sort(reverse=True)#descending
# print(a)


# print(fruits.index('pineapple'))

# --------------------------------------------------------------------------------->


# Create a list of squares from 1 to 10 

# Filter all even numbers from a list 

# Remove all duplicate values from a list.

# Print only unique elements from a list.

# Given a list of names, print only names longer than 5 characters.

# Replace all negative numbers in a list with 0.

# Find the second largest number in a list.

# Split a list into two lists – one with even and one with odd numbers.

# Create a list of only vowels from a list of characters.


# Check if two lists have any common elements.


# ------------------------------------------------------------------------------------------->

# n=5
# a,b=0,1
# fb_list=[]

# count=0
# while count<n+1:

   
#    fb_list.append(a)
#    a,b=b,a+b
#    count+=1


# print("fibinocci list:",fb_list)

# ----------------------------------------------------------------------------------------->


# n=10
# fb_list=[]


# for i in range(1,n+1):
#     fb_list.append(i)

# print(fb_list)
    
# n=100
# fb_list=[]

# for i in range(2,n+1,2):

#     fb_list.append(i)

# print(fb_list)

# ------------------------------------------------------------------------------------------------->

# # dublicate numbers

# numbers=[1,1,2,3,4,2,5,7,3,8,9]

# dublicate=[]

# for i in numbers:
#     if numbers.count(i)>1 and i not in dublicate:
#         dublicate.append(i)

# print(dublicate)

# ------------------------------------------------------------------------------------------------------>

numbers=[1,1,3,4,5,6,7,8,4,5,7,]

unique=[]

for i in numbers:
    if numbers.count(i)==1 :
        unique.append(i)
print(unique)

# ------------------------------------------------------------------------------------------------------->
#longer than 5 characters

# names=["deepak","laksh","hussain","nikil","aravind","saraf","alzhagu","shiv","abi"]

# for name in names:
#    if len(name)>5:
#       print(name)


# ------------------------------------------------------------------------------------------------------->

# num=-10

# negative=[]

# for i in range(0,num-1,-1):
#     negative.append(i)

# print(negative)

#----------------------------------------------------------------------------------------------------------->

#second largest number

# numbers=[10,20,40,50,70,100,110,200]

# largest=max(numbers)
# numbers.remove(largest)
# second_largest=max(numbers)

# print(second_largest)

# number= [10,20,30,10,25,30,70,60,80]
# number.sort()

# print("second largest number;-",number[-2])

#------------------------------------------------------------------------------------------------------->

# num=100

# even=[]
# odd=[]

# for i in range(1,num+1):
#     if i%2==0:
#         even.append(i)
#     elif i%2!=0:
#         odd.append(i)
#     else:
#         break

# print(even)
# print(odd)

#------------------------------------------------------------------------------------------------------>
