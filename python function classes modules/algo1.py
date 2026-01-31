class emp: 
    name='Harsh'
    salary='25000'
    def show(self): 
        print (self.name) 
        print (self.salary) 
e1 = emp() 
# Use getattr instead of e1.name 
print (getattr(e1,'name')) 

emp.salary='30000'
print(emp.salary)