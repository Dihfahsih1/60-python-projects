  
animals = ['dog','zebra','elephant', 'lion',]
def reverse_len(s):
  return -len(s)
y=sorted(animals, key=reverse_len)
 
# lambda function = <para_list>:<expression>

result=(lambda a,b,c: (a+b+c)/4)(10,40,5)
print("lamda function: " + str(result))

std=sorted(animals, key=lambda s: -len(s))
using_sort = animals.sort()

print(using_sort)
