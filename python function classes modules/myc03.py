# Objects can also contain methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
  def myfunc(self):
    print("Hello my name is " + self.name)   ## method

p1 = Person("John", 36)
p1.myfunc()
