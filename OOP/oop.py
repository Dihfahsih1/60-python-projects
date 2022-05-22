class Employee:
  raise_amt = 100
  def __init__(self, first, last, pay):
    self.fname = first 
    self.lname = last 
    self.email = self.fname + "." + self.lname + "@email.com"  
    self.pay = pay
    
  def fullname(self):
    return '{} {}'.format(self.fname, self.lname)
  
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)
  
  def __repr__(self):
    return "Employee('{}', '{}', '{}')".format(self.fname, self.lname, self.pay) 
  
  def __str__(self):
    return '{} - {}'.format(self.fullname, self.email) 
class Developer(Employee):
  raise_amt = 1.10
  def __init__(self, first, last, pay, pro_lang):
    super().__init__(first, last, pay)
    self.pro_lang = pro_lang

class Manager(Employee):
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees
    
  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)
    
  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp) 
      
  def print_emp(self):
    for emp in self.employees:
      print('-->', emp.fullname())
  
 
    
        

emp = Employee("John", "Smith", 700000)
dev_2 = Employee("Yokana", "Nartin", 49999) 

print(str(dev_2))

# mgr = Manager("Patrick", "Aine", 300000, [dev_2])
# print(mgr.email)
# mgr.remove_emp(dev_1)
# mgr.print_emp()
#print(dev_1.pro_lang)
# dev_1.apply_raise()
# print(dev_1.pay)


    