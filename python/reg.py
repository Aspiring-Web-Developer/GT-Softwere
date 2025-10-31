import re

sentence='this is deepak and username is deep123 and number is 9877897978 and tocken 67gbh'

print(re.findall(r'\d',sentence))
print(re.findall(r'\d+',sentence))

print(re.findall(r'\b\d+\b',sentence))#boundry


print(re.sub(r'\d{10}','XXXXXXXXX',sentence))


name='Mr.Venkat'
nampattern=r'(Mr|Ms|Mrs)\.([a-zA-Z]+)'

namecheck=re.match(nampattern,name)

print(namecheck.group(1))



email='shivani12@gmail.in'
epat=r'^[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,3}$'

if re.match(epat,email):
    print('valid email')
else:
    print('invalid email')



print(re.search(r'\d{10}',sentence))

ph='2123456780'

phval=r'[6-9][0-9]{9}'

if re.match(phval,ph):
    print('valid phno')
else:
    print('invalid phno')