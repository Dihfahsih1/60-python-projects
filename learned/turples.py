percent = (30,89,90)

#turples are not mutable

#they can also be created without using parenthesis
b = 12, "turple", 50

#you can assign sequences to a turple
c = (12, 32, 10, 3, "list")
#1, 2, 3, 4, 5 = c

a = 1  
d = 1,

#a and d are different => type: int and type: turple respectively.

print (type(a))

print (type(d))

#turple may contain items of different data types
j= (1, 2.0,'three', ["list","turple"])


#you can only concatenate tuple to a tuple not any other type to a tuple
j + d
print(j)

#though tuples are immutable but if the item in the tuple are a list, they can be changed
j[3][0] = 'tuple' 
j[3][1]= 'list'

print(j.index('three'))

