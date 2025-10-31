#Find the first non-repeating character in a string
input="aaabbbcddd"

for i in input:
    if input.count(i)==1:
     print("the single charcter",i)

#--------------------------------------------------------------------------->
#Write a program to print a hollow square pattern using loops.

n=5
for i in range(n):
   for j in range(n):
      if i==0 or i==n-1 or j==0 or j==n-1:
         print("*",end="")
      else:
           print(" ",end="")
   print()

#--------------------------------------------------------------------->

#anagram
a= "listen"
b="silent"

a1=True

for i in a:
    if i not in b or len(a)!= len(b):
        a1=False
        break
if a1:
    print("True")
else:
    print("not anagram")
#----------------------------------------------------------------------------->
#Reverse the string

sentence = "I love React"


words = sentence.split()  


reversed_words = []
for i in range(len(words)-1, -1, -1):
    reversed_words.append(words[i])

reversed_sentence = ' '.join(reversed_words)

print(reversed_sentence)

#-------------------------------------------------------------------------------------->
#Find the longest word in a string
word2="Learning Python is fun"
word3=word2.split()
longest_word=""
for i in word3:
    if len(i)>len(longest_word):
        longest_word=i
print(longest_word)


    
