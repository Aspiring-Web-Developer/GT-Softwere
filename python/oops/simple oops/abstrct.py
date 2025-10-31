from abc import ABC, abstractmethod

# class bank:
#     def __init__(self,name,acc,ifsc):
#         self.name=name
#         self.acc=acc
#         self.ifsc=ifsc
#         self.balance=500
 
#     def deposit(self):
#         pass
        

class product(ABC):
    elect_count=0
    cloth_count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        
        return f'Name{self.name} Price{self.price}'
    
    @abstractmethod
    def bill(self):
        pass
    
class electronics(product):
    def __init__(self, name, price,Waranty_Years):
        super().__init__(name, price)
        self.Waranty_Years=Waranty_Years
    def __str__(self):
        return  f'Name{self.name} price{self.price} Waranty{self.Waranty_Years}'
    def bill(self):
        print(self.price-500)
    


e=electronics('lg',120000,5)
print(e)
   
e.bill()
