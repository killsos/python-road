class Person(object):
  def __init__(self, name):
    self.name = name
    self.pet = None

class Employee(Person):
  def __init__(self, name, salary):
    super(Employee, self).__init__(name)
    self.salary = salary
  
frank = Employee('ql', 20000000)

print frank.salary