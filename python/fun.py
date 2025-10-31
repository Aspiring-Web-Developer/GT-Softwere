
# def reverseStr(text):
   

#     rev=""

#     for i in range(len(text)-1,-1,-1):
#       rev+=text[i]
#     #  rev=rev+text[i]

#     print(rev)
# reverseStr()

#     if text==rev:
#       print('palin')
#     else:
#       print('not palin')



# reverseStr('hello')
# reverseStr('madam')


def simpleclac(a,b,opr): #parameters
     if opr=='add':
       print(a+b)
     else:
         print(a-b)

simpleclac(10,20,'add')#arguments


# def greet():
#     print('hellow')


# greet()


# *args => we don't know the number of parameters

def totalmarks(*mark):
    print(mark)#recived the value in the form of tuple
    print(f"sum{sum(mark)}")
    print(max(mark))


totalmarks(10,20,30,40,60)

def kewyargmnts(**kwargs): #keyword argument
    print(kwargs)#reciv like dict

kewyargmnts(name='deepak',age=20)