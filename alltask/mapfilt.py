
# ðŸ§  Practice Tasks using map(), lambda, def
# ðŸ”¸ Task 1: Convert all strings in a list to uppercase
# ðŸ”¸ Task 2: Add 5 to every element in the list
# ðŸ”¸ Task 3: Convert a list of temperatures in Celsius to Fahrenheit
# ðŸ”¸ Task 4: Square of all even numbers in the list
# ðŸ”¸ Task 5: Extract first character from each string in a list
# ðŸ”¸ Task 6: Get length of each word
# ðŸ”¸ Task 7: Multiply corresponding items in two lists
# ðŸ”¸ Task 8: Remove spaces from each string

# ðŸ§  Practice Tasks using filter() + lambda / def
# ðŸ”¸ Task 1: Filter only even numbers from the list
# ðŸ”¸ Task 2: Filter words with length > 4
# ðŸ”¸ Task 3: Filter numbers greater than 50
# ðŸ”¸ Task 4: Remove empty strings from a list
# ðŸ”¸ Task 5: Filter names starting with 'A'
# ðŸ”¸ Task 6: Keep only positive numbers
# ðŸ”¸ Task 7: Keep only palindromes from a list
# ðŸ”¸ Task 8: Filter values divisible by 3

#task1

# stri=["deepak,aadhav,praveen,"]
# newstri=list(map(lambda x: x.upper(),stri))
# print(newstri)

#task2

# num=[1,2,3,4,5]
# newnum=list(map(lambda x:x+5 ,num))
# print(newnum)

#task3

# celsious=[35]

# faranheat=list(map(lambda x:(x*9/5)+32,celsious))
# print("faranheat",faranheat)

#task4

# num=[1,2,3,4,5,6,7,8,9,10]

# newnum=list(map(lambda x :x**2,filter(lambda x:x%2==0,num)))

# print(newnum)

#task5

# names=["lakshma","nikil","aasif"]

# newname=list(map(lambda x:x[0],names))

# print(newname)

# task6

# length=["deepak","aasif","nikil","laks"]

# newlengnt=list(map(lambda x: len(x),length))

# print(newlengnt)

# task7

# list1=[12,40,60,20]
# list2=[20,40,30]

# multiple=list(map(lambda x,y:x*y,list1,list2))

# print(multiple)

# names=["deep ak","aash if","nik il","la kh"]

# newnames=list(map(lambda x: x.replace(" ",""),names))

# print(newnames)





#filter

num1=[1,2,3,4,5,6,7,8,9,10]

newnum=filter(lambda x:x)