#whileloop

num=1
total=0

while num<=100:
    total+=num
    num+=1
    print("Sum of number 1 to 100:",total)


#maximumelements

numbers = [40,30,50,60,80,20]
maximum=numbers[0]

for i in numbers:
    if i>maximum:
      maximum=i
print("maximum number is",maximum)

#find large number

a=40
b=30
c=50

if a<=b and a<=c:
   print("the largest number is",a)
elif b<=a and b<=c:
   print("the largest number is",b)
else:
    print("the largest number is",c)