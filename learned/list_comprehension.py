
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
def func1(n):
    return n*n
#use map and lambda function
numbers=(2,3,5,6)
y=map(lambda x:x*x, numbers)
print(list(y))

books=['Genesis', 'Exodus', 'Joshua', 'Numbers', 'Deauteronomy','Leviticus','Judges','Esther','Ruth']

for index, book in enumerate(books,start=1):
    print(index, book)