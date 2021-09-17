
#list comprehension
print([i for i in 'anxiety'])

#ordinary way of iterating the list
mylist = []
for i in "anxiety":
    mylist.append(i)
print(mylist)

#conditioned list comprehension
print([i for i in range(20) if i%2==0 if i%3==0])

print(['Even' if i%2==0 else 'Old' for i in range(8)])

#nested for loop for list comprehension
for i in range(7,9):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
