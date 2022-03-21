class Parent:
  def assign_name(self, name):
    self.name = name
    
  def assign_age(self, age):
    self.age = age
    
  def show_age(self):
    return self.age
    
  def show_name(self):
    return self.name
    
class Child(Parent):
  def __init__(self, study, grow):
      super().__init__(study, grow)
      self.study = study
      self.grow = grow
      
  def studying(self):
    print(self.study + 'is educated')
child1 = Child.talk()

  