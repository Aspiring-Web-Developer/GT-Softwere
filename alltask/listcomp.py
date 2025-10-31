# #1. Create a list of first 10 natural numbers.[1, 2, 3, ..., 10]

# ten=[x for x in range(1,11)]
# print(ten)
# #---------------------------------------------------------------------------->
# #2. Get squares of numbers from 1 to 10.

# square=[x**2 for x in range(1,11)]
# print(square)

# #------------------------------------------------------------------------------>
# #3. Filter odd numbers from 1 to 20.

# odd=[ x   for x in range(1,20) if x%2!=0]
# print(odd)

# #------------------------------------------------------------------------->
# #4. Extract words with more than 4 characters from a list.
# char=['deepak','aashif','ram','abd','yyy']
# more=[x for x in char if len(x)>4]
# print(more)

# #--------------------------------------------------------------------->
# #5. Convert a list of strings to lowercase.
# char2=['DEEPAK','LAKSHMANAN','JAI','VEl']
# low=[x.lower() for x in char2 ]
# print(low)

# #--------------------------------------------------------------------->
# #6.Create a list of numbers from 1 to 50 divisible by 5.
# num=[x for x in range(1,51) if x%5==0]
# print(num)

# #----------------------------------------------------------------------->
# #7. Given a list of words, get the length of each word.
# word=["deepak","lakshmana","venkat"]
# word2=[len(x) for x in word]

# print(word2)

#----------------------------------------------------------------------------->
# #8. From a sentence, extract all words starting with a vowel.
# word3=["deepak","lakshmana","avenkat"]
# vow=[x for x in word3  if x[0] in 'aeiouAEIOU']
# print(vow)

#------------------------------------------------------------------------------>

# 9. Replace negative numbers with 0 in a list.
# lis=[1,20,-1,89,-5,-7]
# negative=[0 if x<0 else x for x in lis]
# print(negative)

#---------------------------------------------------------------------------->

#10. From a list of marks, assign "Pass" if â‰¥ 50, else "Fail".
# mark=[20,70,81,39,49]
# result=[ f'{x} pass' if x>50 else f'{x} fail' for x in mark  ]
# print(result)

#----------------------------------------------------------------------->
#genrate all pairs x,y where x in [1,2] and y in [3,4]
# output:
# [1,3]
# [1,4]
# [2,3]
# [2,4]
# result=[[x,y] for x in [1,2] for y in [3,4]]
# print(result)
#-------------------------------------------------------------------->