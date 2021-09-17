
#list comprehension
print([i for i in 'anxiety'])

#ordinary way of iterating the list
mylist = []
for i in "anxiety":
    mylist.append(i)
print(mylist)

#conditioned list comprehension
print([i for i in range(20) if i%2==0 if i%3==0])
