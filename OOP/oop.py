class Employee:
  raise_amt = 0
  def __init__(self, first, last, pay):
    self.fname = first 
    self.lname = last 
    self.email = self.fname + "." + self.lname + "@email.com"  
    self.pay = pay
    
  def fullname(self):
    return '{} {}.format(self.fname, self.lname)'
  
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)
    
class Developer(Employee):
  raise_amt = 10.5

dev_1 = Developer("Django", "Python", 700000)
 
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

    