var1 ="hello"
var2 = " world"

print(var1.__add__(var2))

class Sumlist(object):
  def __init__(self,mylist):
    self.mylist = mylist
  def __add__(self, other):
    new_list = [x+y for x,y in zip(self.mylist, other.mylist)]
    return Sumlist(new_list)
  def __repr__(self):
    return str(self.mylist)
a=Sumlist([12,34,56])
b=Sumlist([1,24,67,98,90])
print(a+b)