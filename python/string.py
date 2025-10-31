# lang='python language'
# print(lang)
# print(lang[1])
# print(len(lang))

# #one format to another format

# print(lang.capitalize()) #P
# print(lang.title()) #P L
# print(lang.lower())
# print(lang.upper())
# print(lang.swapcase())


# word='  hello  '
# print(word)

# print(word.strip())#it will remove unwanted space befor and after the word
# print(word.lstrip())
# print(word.rstrip())

# print(lang.startswith('p'))
# print(lang.endswith('p'))

# # print(lang.index('Z')) #it will return the index value but if it not present means it will throw error
# print(lang.find('Z'))


# #checking conditiona
# num='13232'
# a='abe 123'
# b='abc'
# c=" "

# print(num.isalpha())
# print(b.isalpha())


# print(a.isalnum())
# print(num.isdigit())#only numbers inside string
# print(b.islower()) #it willcheck wheather the give str is small leters uh?
# #like wise we hae upper, title, capi
# print(c.isspace())


# #iterate the string seperate caps in one list and small letter in one list
# #reverse the string using forloop (without default method)
# #i need output like this helloworld =>HeLlOwOrLd



# newstr=""

# for i in range(len(lang)):
#     if i%2==0:
#         print(i)
#         newstr+=lang[i]


# print(newstr)

# name="deEpAk"

# capital=[]
# small=[]


# for i in name:
#     if i.isupper():
#         capital.append(i)
#     elif i.islower():
#          small.append(i)
# print(capital)
# print(small)


# name="lakshmanan"
# for i in range(len(name)-1,-1,-1):

#     print(name[i])


name="hello world"

result=""

for i in range (len(name)):
    if i%2==0:
        result+= name[i].upper()
    else:
        result+= name[i].lower()
       
print(result)
    