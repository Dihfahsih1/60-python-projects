
a = {1, 2, 3, 4, 5,12, "mugoya", ('love',24), 5}
print(a)

# a set is a sequence of items separated by a comma but it can not be indexed.

# a list might conatain values of different types

# it can not also contain duplicate values

#a = {1, 2, 3, 4, 5, ["list", 'd', 5], {1, 35, "you"}}
# a set is mutable(can be changed but can not contain a mutable list or sets or dictionary)

#Creating a set using a set() keyword

b = set(a) #and not b={a}
for i in b:
    print(i)

#the setfunction set() takes only one arguement which should be iterable
#the set also arranges the items into asceding order
#the set function can also contain an iterable list eg 
c = set(["john", 23, "yokana"])
for i in c:
    print(i)
 
#sets can not be sliced since they don't support indexing

#SET DELETION
#a method must be called on a set
numbers = {1, 3, 5, 70, 9}

#1.use discard(element)
numbers.discard(5) #ignores if the item does not exist

#2. use remove(elerment)

numbers.remove(3) #raises a keyError error if the item doesnot exist

#3. use pop()
#it does not take any arguement
print(c.pop())

#clear()
#this ill empty the set
print(c.clear())

#UPDATING SET
#we use add() and update() methods

#1. add() it adds a single element at the end of the last element in the set
c.add("mathew") #if you add an item that exists, then the set remains unchanged
print(c)

#2. update(), this function adds multiple elemnts to the set

c.update("Mark", "Luke", "Acts")

#python functions on a set => len, max, min, sum, any, all, sorted(). All these don't alter the set but just offer computation

#python methods on a set => in addition to add, update, remove, clear and pop() these may change the state of a set if applied to it

#union, difference

#union on set, it combines all sets together, removing all duplicates

old = {'Genesis', "Exodus", "Numbers", "God", "Command"}
new = {'Mathew', 'Mark', 'Luke', 'John', "God", "Grace"}

books = old.union(old, new)
print(books)


#intersection, returns common elements
print(old.intersection(new))

#difference,returns elements that are unique to a given set

print(new.difference(old))


#symmetric_difference, returns elements that are unique to each set

print(new.symmetric_difference(old))


print(new.intersection_update(old))




