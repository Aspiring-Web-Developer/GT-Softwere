class bank:
    def __init__(self,name,accno,balance):
        self.name=name #public
        self._accno=accno #protected
        self.__balance=balance  #private
    
    def details(self):
        print(f'name-{self.name}')
        print(f'balance-{self.__balance}')
        print(f'accno-{self._accno}')
    
    def changebal(self,val):
        self.__balance=val


cust=bank('raj',2345454545,400)
print(cust)

cust.details()
print(cust.name)

cust.name='deepak'
cust.details()

cust.changebal(10000)
cust.details()

print(cust._accno)
# print(cust.__balance)


