# from abc import ABC, abstractmethod
# class potato_motors:
#     def __init__(self,brand,model,speed):
#         self.brand=brand
#         self.model=model
#         self.__speed=0
#         pass
#     def __str__(self):
#         return f'Brand {self.brand} Model {self.model} speed{self.__speed}  '
    
#     @abstractmethod
#     def show_details(self):
#         pass
#     def get_speed(self):
#         return self.__speed
#     def set_speed(self,limit):
#         self.__speed=limit

# class car(potato_motors):
#     def __init__(self, brand, model, speed):
#         super().__init__(brand, model, speed)
        
#     def __str__(self):
#         return f'Brand {self.brand} Model {self.model} speed{self.__speed} '
#     def show_details(self):
#         print(f'Brand {self.brand} Model {self.model} speed{self.get_speed()}')
        
# class bike(potato_motors):
#     def __init__(self, brand, model, speed):
#         super().__init__(brand, model, speed)
        
#     def __str__(self):
#         return f'Brand {self.brand} Model {self.model} speed{self.__speed} Engine CC {self.Enginecc}'
#     def show_details(self):
#         print(f'Brand {self.brand} Model {self.model} speed{self.get_speed()} ')

# cust1=car("BMW","X5",300)
# cust1.set_speed(280)
# cust2=bike("Yamaha","MT-15",300)
# cust2.set_speed(200)
# cust1.show_details()
# cust2.show_details()
#------------------------------------------------------------------------------->

# 🍔 Student Assignment: Food Ordering System Using OOP
# 🎯 Objective

# Create a simple Food Ordering System where a customer can select multiple food items (Burger, Pizza, Drink), view their details, and calculate the total price.

# Through this project, you will learn to implement the following OOP concepts:

# Encapsulation → Protect sensitive data like price.

# Abstraction → Define a base class that outlines what all food items must have.

# Inheritance → Reuse the base class for different food types.

# Polymorphism → Same method (show_details) behaves differently for each food type.

# Aggregation → Customer has a cart containing multiple food items.

# 🧩 Step-by-Step Instructions
# 🥇 Step 1: Create an Abstract Base Class

# Class Name: FoodItem

# Add private attributes for name and price.

# Create getter methods for each attribute to access them safely.

# Define an abstract method show_details() — all subclasses must implement it.

# Concepts demonstrated: Abstraction + Encapsulation

# 🥈 Step 2: Create Derived Classes

# Burger

# Attributes: size (small / medium / large)

# Implement show_details() to display all info.

# Pizza

# Attributes: toppings (list)

# Implement show_details() to display name, toppings, and price.

# Drink

# Attributes: volume (in ml)

# Implement show_details() to display name, volume, and price.

# Concepts demonstrated: Inheritance + Polymorphism

# 🥉 Step 3: Create a Customer Class

# Attributes:

# name

# cart (a list of FoodItem objects)

# Methods:

# add_to_cart(item) → adds a food item to the cart

# show_cart() → displays all food items and calculates total price

# Concepts demonstrated: Encapsulation (cart management) + Aggregation

# ⚙️ Step 4: Main Program Flow

# Create a Customer object.

# Create instances of Burger, Pizza, and Drink.

# Add them to the customer’s cart.

# Display the final cart with total price using show_cart().

# Concept demonstrated: Polymorphism in action (since show_details() works differently for each item)

# Expected Outcome

# The program should print each item’s details correctly, showing unique info for each food type.
# The total price should also be calculated accurately.

from abc import ABC, abstractmethod

# class DeepZHut(ABC):
#       def __init__(self,name,price):
#             self.__name=name
#             self.__price=price
#       def __str__(self):
#             return f'Name{self.__name} Price{self.__price}'
            

#       def getter_food(self,food):
#             self.__name=food
            
#       def get_amnt(self,amnt):
#             self.__price=amnt

#       def get_name(self):
#             return self.__name
      
#       def get_price(self):
#             return self.__price


#       def addprice(self,amnt):
#             self.__price+=amnt
#             print("Ubdated Price",self.__price)

#       @abstractmethod
#       def show_details():
#             pass

# class burger(DeepZHut):

#       def __init__(self, name, price,size):
#             super().__init__(name, price)
#             self.size=size
            
      
#       def show_details(self):
#              print(f"Name: {self.get_name()}, Price: {self.get_price()}, Size: {self.size}")

#       def add_topings(self,*toppings):
            
#             for i in toppings:
                  
#                   if i=='cheese':
#                         self.addprice(10)
#                         # DeepZHut__price+=10
#                   elif i=='olives':
#                         self.addprice(30)
#                         pass
#                   else:
#                         pass
#                         # DeepZHut__price+=0
#                     # print(i,DeepZHut__price)                  
            
# # b1=burger('normalburger',100,'medium')
# # print(b1)
# # b1.addtopings('olives','cheese')
# # print(b1)


# class pizza(DeepZHut):

#       def __init__(self, name, price,toppings):
#             super().__init__(name, price)
#             self.toppings=[toppings]
            
      
#       def show_details(self):
#              print(f"Name: {self.get_name()}, Price: {self.get_price()}, Size: {self.toppings}")
#       def add_topings(self,*toppings):
            
#             for i in toppings:
                  
#                   if i=='cheese':
#                         self.addprice(10)
#                         # DeepZHut__price+=10
#                   elif i=='olives':
#                         self.addprice(30)
#                         pass
#                   else:
#                         pass
# class Drinks(DeepZHut):

#       def __init__(self, name, price,volume):
#             super().__init__(name, price)
#             self.volume=volume
            
      
#       def show_details(self):
#              print(f"Name: {self.get_name()}, Price: {self.get_price()}, volume: {self.volume}")
      
# class customer:
#       def __init__(self,Name):
#             self.Name=Name
#             self.cart=[]
      
      # def add_order(self, order):
      #   self.cart.append(order)
      #   print(f" Added {order.get_name()} to {self.Name}'s cart.")

#       def view_cart(self):
#         print(f"\n{self.Name}'s Cart Items:")
#         for item in self.cart:
#             item.show_details()
      
#       def generatebill(self,name):

#             bill=0
#             for item in self.cart:
#                bill+=item.get_price()
#             #    print(item.get_price())
#             print(name,bill)


   
# b1 = burger('Normal Burger', 100, 'Medium')
# b1.add_topings('olives', 'cheese')
# b1.show_details()

# p1 = pizza('Paneer Pizza', 200, ['Cheese', 'Capsicum'])
# k1 = Drinks('Mojito', 80, "250ml")

# cust1 = customer('Laks')
# cust1.add_order(b1)
# cust1.add_order(p1)
# cust1.add_order(k1)

# cust1.view_cart()

# cust1.generatebill("Laks Your Total Bill is")

# print()
# d1=pizza("Bread Pizza",200,"cheese")
# d1.add_topings("Cheese")

# d2=Drinks("watermelon",70,"120ml")

# cust2=customer("deepak")
# cust2.add_order(d1)
# cust2.add_order(d2)

# cust2.view_cart()



# cust1=customer('laks',[b1])

# cust1.view_cart_items()
# cust1.addmoreorder()
# print(cust1)


#veichle rental system

class maz_Rental(ABC):
    def __init__(self,Veichle,Days):
        
        self.__Veichle=Veichle
        self.__Days=Days
        
       
    
    def __str__(self):
          return f'Veicle {self.__Veichle} Days {self.__Days}  '
    

    
    def day(self):
         return self.__Days
    def veichle2(self):
          return self.__Veichle
    def addprice(self,amnt):
         self.price+=amnt
         print("Ubdated Price",self.price)
    @abstractmethod
    def All_details():
          pass
    
   
class car(maz_Rental):
      def __init__(self,Veichle, Days,varient,gear,seats):
            super().__init__( Veichle, Days)
            self.Varient=varient
            self.gear=gear
            self.seats=seats
            
      def tlseats(self):
            if self.seats>0 and self.seats<=4:
                price=1000
                total=price*self.day()

                print("You Booked",self.seats,"seats")
                print("And it Price Cost per day:-",price)
                print("The total cost is",total)
            
            elif self.seats>4 and self.seats<=6:
                price=2000
                total=price*self.day()
                print("You Booked",self.seats,"seats")
                print("And it Price Cost per day:-",price)
                print("The total cost is",total)
            elif self.seats>6 and self.seats<=9:
                  price=3000
                  total=price*self.day()
                  print("You Booked",self.seats,"seats")
                  print("And it Price Cost per day:-",price)
                  print("The total cost is",total)
            else:
                  print("9 more seats not available")
      
      def All_details(self):
          
          print(f'You Booked Veichle {self.veichle2()}')
          print(f'Yor varient {self.Varient}')
          print(f'Gear Type {self.gear}') 
          print(f'Total seats:- {self.seats}')
          

class Bike(maz_Rental):
      def __init__(self, Veichle, Days,license):
            super().__init__(Veichle, Days, )
            self.license=license
      
      def BikeType(self,Type):
            if Type=="Scooty":
                price=1000
                total=price*self.day()
                print("You Booked",Type)
                print("And it Price Cost per day:-",price)
                print("The total cost is",total)
            elif Type=="Bike":
                price=1500
                total=price*self.day()
                print("You Booked",Type)
                print("And it Price Cost per day:-",price)
                print("The total cost is",total)
      
      def All_details(self):
          
          print(f'You Booked Veichle {self.veichle2()}')
          
          print(f'Your license no{self.license}') 

class customer:
      def __init__(self,name,details):
            self.name=name
            self.details=details
            self.booked=[]
      def __str__(self):
            return f'Name {self.name} Aadhar num {self.details} '
      def add_order(self, order):
         self.booked.append(order)
         print(f" Added {order} to {self.name}'s Trip.")

      
      def view_cart(self):
          print(f"\n{self.name}'s booked veichle:")
          for item in self.booked:
             item.All_details()
      
    

c1=car("Car",3,"Top Varient","Automatic")
c1.All_details()


custom=customer()
print(custom)
custom.view_cart()
custom.add_order(c1)


