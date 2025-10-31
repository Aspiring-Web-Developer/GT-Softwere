# Regex Practice Questions

# Write a regex that ensures a string contains at least one lowercase letter.

# Write a regex that ensures a string contains at least one uppercase letter.

# Write a regex that ensures a string contains at least one digit.

# Write a regex that ensures a string contains at least one special character from [!@#$%^&*].

# Write a regex that ensures a string contains at least one lowercase, one uppercase, one digit, and one special character, and is minimum 8 characters long.

# Write a regex that ensures a string does not contain consecutive repeating characters.

# Write a regex that ensures a string starts with a letter and contains at least one digit anywhere.

# Write a regex that ensures a string does not contain spaces but contains at least one uppercase and one lowercase letter.

# Write a regex that ensures a string contains either cat or dog, but not both.

# Write a regex that ensures a string does not start or end with a special character but contains at least one digit.

import re

# setpass=r'(?=.*[a-z])'

# passw="DEEpAK"

# if re.match(setpass,passw):
#     print("valid")
# else:
#     print("invalid")
#-------------------------------------------------------------------------------------->

# setpass=r'(?=.*[A-Z])'
# passw="Deepak"

# if re.match(setpass,passw):
#     print("valid")
# else:
#    print("invalid")

#-------------------------------------------------------------------------------------->

# setpass=r'(?=.*\d)'
# passw="deepak1"

# if re.match(setpass,passw):
#     print("valid")
# else:
#    print("invalid")
#------------------------------------------------------------------------------------->

# setpass=r'(?=.*[@!#$%^&*()_])'
# passw="Deepak"
# if re.match(setpass,passw):
#     print("valid")
# else:
#    print("invalid")

#---------------------------------------------------------------------------------->
# setpass=r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*_()])[a-zA-Z\d!@#$%^&*()_]{8,}'
# passw="Deep@k01"
# if re.match(setpass,passw):
#     print("valid")
# else:
#    print("invalid")

#------------------------------------------------------------------------------------>

setpass=r'(?=.*(.)\1+)'
passw="Deepak"

print(re.findall(r"(.)\1+",passw))


if re.match(setpass,passw):
    print("valid")
else:
   print("invalid")

#-------------------------------------------------------------------------------------->
# setpass=r'^\D+(?=.*\d)\d{1,}'
# passw="Deepak12"
# if re.match(setpass,passw):
#     print("valid")
# else:
#    print("invalid")

#------------------------------------------------------------------->

setpass=r'^(?=.*[a-z])(?=.*[A-Z])\S+$'
passw="Deepak123"

if re.match(setpass,passw):
    print("valid")
else:
   print("invalid")

#----------------------------------------------------------------------->

# passw="I have a  and dog "

# pattern=re.compile(r'^(?=.*\b(?:cat|dog)\b)(?!.*\bcat\b.*\bdog\b)(?!.*\bdog\b.*\bcat\b).+$')

# print(bool(pattern.match(passw)))

#--------------------------------------------------------------------------->

# setpass=r'^.*[A-Z](?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()]).*[A-Z]$'
setpass=r'^[A-Z]+(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()]).+[A-Z]$'

passw="#Deep@K"

if re.match(setpass,passw):
    print("valid")
else:
    print("! start or end with spl character")

#------------------------------------END------------------------------------------>