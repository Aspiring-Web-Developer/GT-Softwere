class vinayaga_motors:
    bike_count=0
    car_count=0
    def __init__(self,model,brand,year):
        self.model=model
        self.brand=brand
        self.year=year

    def __str__(self):
        return f'model:-{self.model}brand:-{self.brand}year:-{self.year}'
    
    def greets(self):
        print(f"Thank you for booking veichls from vinayaga motors")

class bike(vinayaga_motors):
    def __init__(self,name, model, brand, year,milage):
        super().__init__(model, brand, year)
        self.name=name
        self.cc=150
        self.milage=milage
        self.gear="manual"
        self.disk="double"

        vinayaga_motors.bike_count+=1
    def __str__(self):
        return f'Name {self.name} Model{self.model} Engine CC{self.cc} Milage{self.milage} gear{self.gear} disk{self.disk}'
   
cust1=bike("lake","mt-15","Yamaha",2025,45)
# print(cust1.greets())
print(cust1)

cust2=bike("deepak","rx-100","yamaha",2018,32)
print(cust2)
print(vinayaga_motors.bike_count)

class car(vinayaga_motors):
    def __init__(self, model, brand, year,typegear,varient,colour):
        super().__init__(model, brand, year)
        self.typegear=typegear
        self.varient=varient
        self.colour=colour
        vinayaga_motors.car_count+=1
    def __str__(self):
        return f'Model{self.model} Brand{self.brand} Year{self.year} Gear{self.typegear} Varient{self.varient} Colour{self.colour}'
    
    
ccust1=car("X5","BMW",2023,"mannual","top","black")
print(ccust1)
ccust2=car("F_pase","Jaguar",2025,"automatic","top","red")
print(ccust2)
print(vinayaga_motors.car_count)

#------------------------------------------------------------------------------>

class person:
    students_count=0
    teacher_count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
           
           return f'name{self.name} age{self.age}'
class student(person):
    def __init__(self, name, age,rollno,grade):
        super().__init__(name, age)
        self.rollno=rollno
        self.grade=grade
        person.students_count+=1
    def __str__(self):
        return f'Name{self.name} Age{self.age} Rollno{self.rollno} Grade{self.grade}'
    
class teacher(person):
    def __init__(self, name, age,subject,salry):
        super().__init__(name, age)
        self.subject=subject
        self.salry=salry
        person.teacher_count+=1
    def __str__(self):
        return f'Name{self.name} Age{self.age} subject {self.subject} salary{self.salry}'
student1=student("Deepak",21,1107,"A")
student2=student("Lake",20,1108,"C")
student3=student("nikhil",18,1106,"B")
print(student1)
print(student2)
print(student3)
print(person.students_count)
teacher1=teacher("aravind",30,"python",25000)
teacher2=teacher("pradheep",30,"javascript",3000)

print(teacher1)
print(teacher2)

print(person.teacher_count)

#--------------------------------------------------------------------->

class product:
    elect_count=0
    cloth_count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        
        return f'Name{self.name} Price{self.price}'
    def bill(self):
        print(self.price-10)
    
class electronics(product):
    def __init__(self, name, price,Waranty_Years):
        super().__init__(name, price)
        self.Waranty_Years=Waranty_Years
    def __str__(self):
        return  f'Name{self.name} price{self.price} Waranty{self.Waranty_Years}'
    def bill(self):#polymorphism supports overriding
        if self.price>5000:
            print(self.price-500)

class cloth(product):
    def __init__(self, name, price,size,material):
        super().__init__(name, price)
        self.size=size
        self.material=material
    def __str__(self):
        return  f'Name{self.name} price{self.price} Size{self.size} Material{self.material}'
    
cust5=electronics("transformer",250,2)

print(cust5)

cust6=cloth("full Hand shirt",850,"XL","cotten")
print(cust6)

#-------------------------------------------------------------------------------->
class bank:
    def __init__(self,accountno,balance):
        self.accountno=accountno
        self.balance=balance
    
        
class saving_account(bank):
    def __init__(self, accountno, balance):
        super().__init__(accountno, balance)
        self.intrest_rate=0.20
    def __str__(self):
        return f'Your Account no {self.accountno} Your Balance{self.balance} your intrest{self.intrest_rate}'
    def intrest(self):
        og_balance=self.intrest_rate*self.balance
        total=og_balance-self.balance
        print("discount",og_balance)
        print(total)
    
class fixed_account(bank):
    def __init__(self, accountno, balance):
        super().__init__(accountno, balance)
        self.duration_years=5
    def __str__(self):
        return f'Your Account no {self.accountno} Your Balance{self.balance} duration{self.duration_years}'

holder1=saving_account(12234455666,5000)      
print(holder1)

#----------------------------------------------------------------------------->
