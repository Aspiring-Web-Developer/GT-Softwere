# class coursedeatail():
#     def __init__(self,name,coursename,duration):
#          self.name=name
#          self.coursename=[coursename]
#          self.duration=duration
         
         
#     def __str__(self):
#          return f"Name-{self.name} Course-{self.coursename} duration-{self.duration} "

#     def addcourse(self,course):
#       self.coursename.append(course)
#       self.duration+=3
     

# Sdetail=coursedeatail("Deepak","Python Fullstack Web developer",3)
# Sdetail.addcourse("javascript")
# sdetail2=coursedeatail("lack","Python Fullstack Web developer",3)
# sdetail3=coursedeatail("nikil","Data Analyst",3)




# print(Sdetail)
# print(sdetail2)
# print(sdetail3)

#---------------------------------------------------------------------------------------->

class cars():
    def __init__(self,car,model,year):
        self.car=car
        self.model=model
        self.year=year
    def __str__(self):
        return f'car-{self.car} model{self.model} year{self.year}'
    def car_info(self):
      print(f"Dear Custmer your car {self.car} and the model is {self.model} version year{self.year}")

    
cardetail=cars("Toyota","camry",2025,)
print(cardetail)
cardetail.car_info()

#--------------------------------------------------------------------------------------------->


class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):

        return f"name:-{self.name} englis:{self.marks[0]} maths:{self.marks[1]} science{self.marks[2]}"
    
    def totalmaks(self):
        total=0
        og_total=total
        for mark in self.marks:
            og_total+=mark
            calculate=og_total/3
        avrg=int(calculate)
            
        print(" total mark",og_total)
        print("avg",avrg)

        if calculate>=35 and calculate<50:
            print("C grade")
            
        elif calculate>=50 and calculate<75:
            print("B Grade")
        elif calculate>75:
            print("A Grade")
        else:
            print("Fail")         
studentdtl=student("Deepak",[70,65,60])
studentdtl2=student("lak",[80,75,65])
studentdtl3=student("nikil",[60,75,80])


print(studentdtl)
studentdtl.totalmaks()

print()
print(studentdtl2)
studentdtl2.totalmaks()

print()
print(studentdtl3)
studentdtl3.totalmaks()

#-------------------------------------------------------------------------------------------------->
class laptop():
    price=0
    proc=""
    ram=""
    def __str__(self):
           return f'price{self.price} proc{self.proc}  ram{self.ram}'
     

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=40000
hp.proc="i7"
hp.ram="8GB ram"

dell.price=60000
dell.proc="i7"
dell.ram="12GB RAM"

lenovo.price=42000
lenovo.proc="i7"
lenovo.ram="8GB RAM"

print("hp",hp)
print("DELL",dell)
print("lenova",lenovo)

#-------------------------------------------------------------------------------------------------->
class book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.availble=True
    def __str__(self):
        
        return f'name:-{self.title} author:-{self.author} avail-{self.availble}'
    
    def borrowbook(self):
        self.availble=False
        

    def returnBook(self):
        self.availble=True
        
    

book1=book('harrypotter','mr.harry')
book2=book('ponnyin selven','kalki')
book3=book('velpaari','kabilar')


book1.borrowbook()
print(book1)

book2.returnBook()
print(book2)

#------------------------------------------------------------------------------>

class employe():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f'name:-{self.name} before salary:-{self.salary}'
    
    def bonus(self):
        salry1=10/100
        salr2=salry1*self.salary
        bonus=salr2+self.salary
        print("Your bonus",salr2)
        print("your current salry",bonus)

    
employe1=employe("lakshmanan",50000)
employe2=employe("lakshmanan",40000)
employe3=employe("nikhil",45000)

print(employe1)
employe1.bonus()
print()

print(employe2)
employe2.bonus()
print()


print(employe3)
employe3.bonus()




        
      





        


       

        
    
        