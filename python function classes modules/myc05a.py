# Add a property graduation year      Add a year parameter
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019     # -> 2019

  def printname(self):
    print(self.firstname, self.lastname)

  def welcome(self):   # method
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)  

x = Student("Mike", "Olsen")
print(x.graduationyear)  #  -> 2019

x = Student("Mike", "Olsen")     
x.welcome()