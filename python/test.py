num=int(input("Enter any number"))
temp=num

sum_of_digit=0

while temp>0:
    digit=temp%10
    sum_of_digit+=digit**3
    temp//=10

if(sum_of_digit==temp):
    print("this number is armstrong")
else:
    print("This number is not armstrong")