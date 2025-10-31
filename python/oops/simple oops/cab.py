class olacabs:
  cust=0
  drivers=0

  def __init__(self,name,email,loc,phno):
    self.name=name
    self.email=email
    self.loc=loc
    self.phno=phno

    
  
  def __str__(self):
    return f'name{self.name} {self.loc} {self.phno}'
  
  def greet(self):
    return f'welcome to olacabs. {self.name} your name registered.'
  

# a=olacabs('avac','ab','chennai',89898898)
# print(a)


class custCabs(olacabs):
   def __init__(self,name,email,loc,phno,gender):
      super().__init__(name,email,loc,phno)
      self.gender=gender
      self.wallet=50
      self.locationhist=[]
      self.charge=0
      olacabs.cust+=1
    
   def __str__(self):
    return f'name{self.name} {self.loc} {self.phno} {self.wallet} {self.gender}'

   def bookcar(self,location,km):
     self.locationhist.append(location)
     print(f'{self.name} you booked car for {location} with {km} km')

   def mydetails(self):
     return f"name{self.name}  {self.wallet} {self.gender} {self.locationhist}"
   

cust1=custCabs('deepak','deep@gmail.com','coimbatore',9978786666,'male')
print(cust1)
print(cust1.greet())


cust1.bookcar('rspuram',15)
print(cust1.mydetails())

cust2=custCabs('deepa','deep@gmail.com','coimbatore',9978786666,'male')
print(cust2)


print(olacabs.cust)


class diverCabs(olacabs):
   def __init__(self,name,email,loc,phno,exp,lis):
      super().__init__(name,email,loc,phno)
      self.exp=exp
      self.lis=lis
      self.star=0
      olacabs.drivers+=1
    
   def __str__(self):
    return f'name{self.name} {self.loc} {self.phno} {self.lis} {self.exp} {self.star}'
   
   def addstar(self,num):
     self.star=num
   
   
drv=diverCabs('arjun','ar@gmail.com','chennai',89766666689,3,True)
print(drv)
drv.addstar(4)
print(drv)
