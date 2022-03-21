class Person(object):
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    
  @property
  def full_name(self):
    # return "%s %s" % (self.first_name,self.last_name)
    print("%s %s" % (self.first_name,self.last_name))
  
  @full_name.setter
  def full_name(self, value):
    parts=value.split()
    if len(parts)==2:
      self.first_name = parts[0]
      self.last_name = parts[1]
    else:
      self.first_name =value
      self.last_name = ""   

p = Person(input('Enter Your name: \n'), input("Enter last name: \n"))

p.full_name