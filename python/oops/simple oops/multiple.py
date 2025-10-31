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
  

class payment:
  
  def __init__(self,upicode,access):
    self.upicode=upicode
    self.accesss=access
    self.mode='online payment'

  def paymentdetails(self):
    print('you have choose',self.mode)

  def changepayment(self,mod):
    self.mode=mod

class custCabs(olacabs,payment):
   def __init__(self,name,email,loc,phno,gender,upicode,access):
      olacabs.__init__(self,name,email,loc,phno)
      payment.__init__(self,upicode,access)
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
   
   def greet(self):
     return 'this is deepak and lak'
   
cust2=custCabs('deepa','deep@gmail.com','coimbatore',9978786666,'male','g5655222',True)
print(cust2)

print(cust2.greet())

# cust2.paymentdetails('cash')
cust2.paymentdetails()

cust2.changepayment('cash')
cust2.paymentdetails()




