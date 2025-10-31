num=[1,2,3,4,5,6]
# newnum=[]

# for i in num:
#     newnum.append(i**2)

newnum=list(map(lambda n: n**2, num))

print(newnum)


fruits = ["apple","jkjls", "banana", "orange", "mango", "grapes", "pineapple"]


newfrts=tuple(map(lambda f: f.title(),fruits))
print(newfrts)


#FILTER

NOTAPPLE=tuple(filter(lambda f: f!='apple',fruits))
print(NOTAPPLE)


numbaboveten=list(filter(lambda n: n>10 and n<30, newnum))

print(numbaboveten)


names=['deepak','lakh','shivani']
marks=[90,89,78]

print(list(zip(names,marks)))


lang='Python is a popular, programming language, used for web, and software development'

print(lang.split())
print(lang.split(','))#convert string to list


print(fruits)

print(' '.join(fruits))#convert list to string