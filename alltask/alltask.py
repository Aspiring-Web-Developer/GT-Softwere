


# # for i in range(1,101):
# #     if i%3==0:
# #         print(i)
   
# # num=[10,20,30,40,50]

# # num2=[]


# # for i in range(len(num)):
# #     each=num[i]
# #     each=each**2
# #     num2.append(each)
# # print(num2)
        
        
# #-------------------------------------------------------------------------------------->

# def each( name):
  
#     empty={}
    
#     for i in name:
#         if i in empty:
#             empty[i]=empty[i]+1
#         else:
#             empty[i]=1
#     print(empty)
# each( input("enter ur name"))


# # def voweln(vowels):
# #     vowel="a","e","i","o","u"
# #     vowels_count=0
# #     for i in vowels:
# #         if i in vowel:
# #           vowels_count=vowels_count+1
# #     print(vowels_count)

# # voweln("deepakakashlakh")

# def dublicates(num):
#    num1=[]
#    for i in num:
#       if i not in num1:
#          num1.append(i)
#    print(num1)
# dublicates([20,30,80,20,30,70,65])
 
# def largenumber(*number):
#    num_of_large=0
#    for i in number:
#       if i >num_of_large:
#          num_of_large=i
#    print(num_of_large)

# largenumber(10,30,40,80,35,60)
# def secondnumber(*number):
#    largest=0
#    second=0
#    for i in number:
#       if i>largest:
#          second=largest
#          largest=i
#       elif i>second :
#           second=i
#    print(largest)
#    print(second)
# secondnumber(10,30,40,80,35,60,90,55,470)

# def largeststr(*string):
#    big=""
#    for i in string:
#       if len(i)>len(big):
#          big=i
#    print("the largest string is:- ",big)
 


# largeststr("apple","range","kollywood","tolly","programming")


# name="deepakakash"

# occurence={}

# for i in name:
#     if i in occurence:
#         occurence[i]=occurence[i]+1
#     else:
#         occurence[i]=1

# print(occurence)

a= "listen"
b="silenk"

a1=True

for i in a:
    if i not in b or len(a)!= len(b):
        a1=False
        break
if a1:
    print("anagram")
else:
    print("not anagram")
    
    