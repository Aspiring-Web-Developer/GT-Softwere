a={}
b=dict.fromkeys(['a','b','c'],0)
print(a)
print(b)
c=dict()
print(c)
user={
    'id':12,
    'name':'deepak',
    'marks':[100,78,34],
    'address':{
        'city':'coimbatore',
        'street':'navaindia'
    },
    'total': lambda :user['marks'][0]+user['marks'][1]+user['marks'][2]

}

print(user.keys())
print(user.values())

# print(user['name'])
# print(user['marks'][1])
# print(user['address']['street'])
# print(user['total']())
# user['age']=20
# print(user)
# user['id']=111
# print(user)

# user.update({'name':'dhoni'})
# print(user)
user.pop('id')#it will remove particualr item

print(user)

user.popitem()#it will remove last added item
print(user)


# fruits = ["apple","jkjls", "banana", "orange", "mango", "grapes", "pineapple"]

# for i in fruits:
#     print(i)



for i in user.keys():
   print(user[i])