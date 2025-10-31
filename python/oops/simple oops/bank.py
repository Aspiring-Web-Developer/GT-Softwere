class Bankdetails():

    def __init__(self,name,accno,address): #if u use __(double underscore means) - dunder methods
        self.name=name
        self.accno=accno
        self.address=address
        self.balance=500
        self.ifsc='SBI10je'
    
    def __str__(self):
        return f"name -{self.name} accno-{self.accno} bal={self.balance}"
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"dear, {self.name} your account is creadited with {amount} and your balance is {self.balance}")

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"dear, {self.name} your account is debited with {amount} and your balance is {self.balance}")
        else:
            print('insuficient amount, try with valid amount')




cust1=Bankdetails('lakshmanan',2787899004,'Navaindia')
print(cust1)
print(cust1.ifsc)
print(cust1.balance)

cust2=Bankdetails('deepak',2787899009,'singanallur')

cust3=Bankdetails('aravind',2787899010,'Navaindia')

cust4=Bankdetails('hussain',2787899011,'rspuram')

cust1.deposit(500)


cust3.withdraw(90)
print(cust1,cust2,cust3,cust4)