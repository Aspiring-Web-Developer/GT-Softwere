class CustomerInfo:
    def __init__(self,name,email,address,):
        self.name=name
        self.email=email
        self.address=address
    def __str__(self):
        return f'name: {self.name} Email: {self.email} Address: {self.address} '

class OrderInfo:
    def __init__(self,orderid,productname,quanity):        
        self.orderid=orderid
        self.productname=productname
        self.quanity=quanity
    def __str__(self):
        return f'orderID: {self.orderid} ProductName: {self.productname} Quantity: {self.quanity}'

class PaymentInfo(CustomerInfo,OrderInfo):
   def __init__(self, name, email, address,orderid,produtname,quanity,payment_method):        
        CustomerInfo.__init__(self,name, email, address)
        OrderInfo.__init__(self,orderid,produtname,quanity)
        self.payment_method =payment_method
   def calculate_method(self,price_per_item):
       total=self.quanity*price_per_item
       if self.quanity>=5:
           discount=total*0.10
           total-=discount
           print(f"Discount applied (10%): ₹{discount}")
       else:
           print("you have Discount")
       return total
       
       

   def show_summary(self,price_per_item):
        print(f'Name: {self.name}')
        print(f'Email:{self.email}')
        print(f'Address:{self.address}')
        print(f'OrderID:{self.orderid}')
        print(f'ProductName:{self.productname}')
        print(f'Quantity:{self.quanity}')
        print(f'Payment Method:{self.payment_method}')
        total = self.calculate_method(price_per_item)
        print(f"Total Amount  : ₹{total}")
    
cust1=PaymentInfo("Deepak","Deepaksadha@gmail.com","Vaagarayampalayam",7896,"rise-25kg",8,"gpay")

cust1.show_summary(1500)

       
    


  