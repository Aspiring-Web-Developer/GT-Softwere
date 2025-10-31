class hospital:
    def __init__(self,name,age,diesease):
        self.name=name
        self.age=age
        self.diesease=diesease
        self.meditions=[]
    
    def __str__(self):
        return f'Name {self.name} Age {self.age} Diesease{self.diesease} '
    def display_info(self):

       print(f'Name {self.name} Age {self.age} Diesease{self.diesease} ')

    def ubdate_diease(self,new_diese):
        self.diesease=new_diese
        self.display_info()
    
    def add_medicon(self,medic):
        self.meditions.extend(medic)
        print("Take this medicine",self.meditions)
    def remove_medicon(self,remove):
        self.meditions.remove(remove)
        print("now you Take this particular medicine",self.meditions)
    def health_check(self):
        print("Now Your condition is better than yesterday")
    def age_group(self):
        if self.age<18:
            print("Child")
        elif self.age>=18 and self.age<60:
            print("Adult")
        else:
            print("Senior")
    def bill(self,days,rate_per_day):
        total=days*rate_per_day
        print("Booked Days",days)
        print("per day our hospital charge is",rate_per_day)
        print("And your Total Bill is ",total,"Thank you for receiving our hospital")
        
pationt1=hospital("deepak",25,"fever")
pationt1.display_info()
pationt1.ubdate_diease("dengu")
pationt1.add_medicon(["dolo","vks500","nilavembu"])
pationt1.remove_medicon("dolo")
pationt1.health_check()
pationt1.age_group()
pationt1.bill(3,3000)