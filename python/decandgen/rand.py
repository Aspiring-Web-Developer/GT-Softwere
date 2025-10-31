import random

print(random.choice(['red','orange','yellow','pink']))
print(random.random())
print(random.randint(1000,9999))

otp=random.randint(1000,9999)
print(otp)

enterotp=int(input('enter otp'))

if otp==enterotp:
    print('otp verified')
else:
    print('invalid otp')



print(random.sample(range(30,50),5))
ar=['a','b','c','d','e','f']
random.shuffle(ar)

print(ar)
print(random.random())
otp=random.randint(1000,9999)
print(otp)

enterotp=int(input('enter otp'))

if otp==enterotp:
    print('otp verified')
else:
    print('invalid otp')

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 100:
        break     # ✅ exits loop safely
print("You entered:", num)
