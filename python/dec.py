def my_decorator(func):

    def creatinburger():
        print('add moyo on first bun')
        func()
        print('add sause on second bun')
    return creatinburger
   

@my_decorator
def greet():
    print('hello world')

greet()