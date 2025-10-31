# œ… 20 Regex Practice Tasks
# ðŸ”¹ Basic Level
# Check if a string contains only alphabets
# Input: "HelloWorld" â†’ âœ…
# Input: "Hello123" â†’ â Œ

# Check if a string contains only digits
# Input: "12345" â†’ âœ…

# Check if a string starts with "ab"
# Input: "abcdef" â†’ âœ…

# Check if a string ends with ".com"
# Input: "example.com" â†’ âœ…

# Extract all digits from a string
# Input: "abc123xyz456" â†’ ['123', '456']

# Check if a string is a valid lowercase word (only lowercase)
# Input: "hello" â†’ âœ…
# Input: "Hello" â†’ â Œ

# Find all words with exactly 4 letters
# Input: "This is a test line" â†’ ['This', 'test', 'line']

# Find all uppercase letters in a string
# Input: "AbCDe" â†’ ['A', 'C', 'D']

# Replace all whitespace with hyphens
# Input: "hello world again" â†’ "hello-world-again"

# Extract the first word of a sentence
# Input: "Learning regex is fun" â†’ "Learning"

# ðŸ”¸ Intermediate Level
# Validate an Indian mobile number
# Condition: 10 digits starting with 6â€“9
# Input: "9876543210" â†’ âœ…

# Validate a simple email format
# Input: "user@example.com" â†’ âœ…

# Extract all words that start with a capital letter
# Input: "My Name Is Bond" â†’ ['My', 'Name', 'Is', 'Bond']

# Find all occurrences of a word â€œappleâ€  regardless of case
# Input: "Apple is tasty. I like apple." â†’ ['Apple', 'apple']

# Check if a string contains a special character (@, _, #, etc.)
# Input: "Hello@123" â†’ âœ…

# ðŸ”º Advanced Level
# Validate a date in dd-mm-yyyy format
# Input: "31-12-2023" â†’ âœ…

# Extract all hashtags from a post
# Input: "Learning #Python and #regex" â†’ ['#Python', '#regex']

# Mask all but last 4 digits of a phone number
# Input: "My number is 9876543210" â†’ "My number is ******3210"

# Find and remove duplicate words
# Input: "This is is a test test line" â†’ "This is a test line"

# Extract domain name from an email address
# Input: "contact@openai.com" â†’ "openai.com"


import re

# name="deepak123"

# print(re.findall(r'\D+',name))

#---------------------------------------------------------------------------->
# number="12345"
# patn=r'^[0-9]+$'

# if re.match(patn,number):
#     print("this is number")
# else:
#     print("thats not only number")
#--------------------------------------------------------------------------------->
# name="abcdf"
# patn=r'^[ab]'

# if re.match(patn,name):
#     print("This start with 'ab'")
# else:
#     print("doesn't start 'ab'")
#------------------------------------------------------------------------------->

# web="deepak.com"
# patn=r'[a-z]+\.[com]{3}$'

# if re.search(patn,web):
#     print("its end with '.com")
# else:
#     print("its not end with '.com")

#----------------------------------------------------------------------------------->

# name="abc123xyz456"

# print(re.findall (r'\d+',name))

#--------------------------------------------------------------------------------->

# name="helloworld"
# patn=r'[a-z]+$'

# if re.match(patn,name):
#     print("valid")
# else:
#     print("Invalid")
#---------------------------------------------------------------------------->

# text="This is a test line"
# print(re.findall(r'\b[A-Za-z]{4}',text))

#----------------------------------------------------------------------------------->

# Input= "AbCDe"

# print(re.findall(r'[A-Z]',Input))
#------------------------------------------------------------------------------------>
# Input= "hello world again"
# print(re.sub(r'[ ]','-',Input)) 

#---------------------------------------------------------------------------------->

# Input= "This is a test  line"
# patnn=re.match(r'\w+',Input)
# if patnn:
#     print(patnn.group())

#------------------------------------------------------------------------------------->


# #Intermediate

# Input="9876543210"
# patn=r'^[6-9][0-9]{9}'

# if re.match(patn,Input):
#     print("Valid num")
# else:
#     print("Invalid")

#----------------------------------------------------------------------->

# input="user@example.com"
# patn=r'^[a-z]+@[a-z]+\.[a-z]{2,3}$'

# if re.match(patn,input):
#     print("EMail Ok")
# else:
#     print("Not ok")

#--------------------------------------------------------------------->

# input= "My Name is Bond"
# print(re.findall(r'[A-Z]{1}[a-z]+',input)) 

#---------------------------------------------------------------------->
# Input="Apple is tasty. I like apple ."

# matches=re.findall(r'apple',Input,re.IGNORECASE)
# print(matches)

#------------------------------------------------------------------------>

# input="Hello@123"
# match=r'[@_#$!&()]+[0-9]+'

# if re.findall(match,input):
#     print("This strin have spl character")
# else:
#     print("NO spl character")
 #--------------------------------------------------------------------------->

# input="10-04-2002"
# match=r'[0-9]{2}-[0-9]{2}-[0-9]{4}'

# if re.match(match,input):
#     print("valid")
# else:
#     print("invalid")


#------------------------------------------------------------------------------------->

input="Learning #Python and #regex"
print(re.findall(r'\W+',input))

