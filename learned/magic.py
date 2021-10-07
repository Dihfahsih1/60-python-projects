var1 ="hello"
var2 = " world"
import pickle

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

year = 2000 
year=input("Enter the Year: ")
int(year)
if(year%4)==0:
  if(year%100)==0:
    if(year%400)==0:
      print(f'{year} is a leaper year'.format(year))
    else:
      print('{0} is not a leaper year')
  