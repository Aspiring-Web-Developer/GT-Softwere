#variables - containeer to store values
#datatypes- int(numbers), string, boolean, list, tuple, dictionary, set

age=12
abcd='hellow'#string
b='sffw'
sum='190'

is_response=True

marks=[10,20,13] #multable -list
score=(1,2,3,4) #immutable tuple
user={
    'id':12,
    'name':'deepak'
}#dict

demo={10,20,20,13,90}#set ignore duplicate values



#variables ->rulesfor naming a variables

# 1. meaningful or resonable name
# 2. shoulnd starting with number, special character and space
# 3. you should not leave a space, first_Name (instead of space use underscore)
# 4. you shouldnt use keyword too


# OPERATORS(+ - * / %(remainder)  //-floor division **-power)

number1=10
number2=12

print(number1/3)#division(complete div) returns quotient
print(number1%3) #remainder
print(number1//3)#floor division (if division answer in decimal means it will round and return)


#comparison operator (==, !=, > , <, >=, <=) ----->return boolean

Shiv_mark=78
Deep_mrk=78

print('greater than', Shiv_mark<=Deep_mrk)

username='admin'

user='adminN'

print(username!=user)



toss='headd'

if toss=='head':
    print('csk won the toss')

if toss=='head':
    print('csk won the toss')
else:
    print('srh won the toss')
    


print(10**3)

#logical operator(and or not)

gender='male'
age=int(input('type your age to check: '))
if gender=='male' or age<50:
    print('eligible for applying scheme')
else:
    print('not eligibl')

###ranging

if age > 0 and age <18:
    print('not elg for vote')
elif age>=18 and age<=75:
    print('eligibile for vote')
else:
    print('senior citizens')



#MEMBERSHIP OPERATOR 
my_name='deepak s'
print('k' in my_name)
print('ki' not in my_name)



num=int(input('type some number '))
print(type(num))
print(num*10)