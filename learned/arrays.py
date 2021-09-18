#An array is a collection of items with the same data type stored at contiguous memory locations

#CREATING AN ARRAY
import array as arr

a = arr.array('i', [1, 3,4])
print("the new array created is: ", end=" ")

for i in range(0, 3):
    print(a[i], end=" ")
print()

#adding elements to the array
#Using insert
a.insert(2, 100)
a.append(200) #using append to insert element
a.insert(4, 100)
print("An array after insertion: ", end=" ")
for i in (a):
    print(i, end = " ")
print()

#Accessing an Array using index operator of []
print(a[2])

#removing elements one at a time

a.append(400)
a.remove(100) #remove the first occurrence of 400

print("An array after removing 100  is : ", end=" " )
for i in (a):
    print(i, end=" ")
print()

#Using pop() to remove element at a specific position

print("poped up element is: ", end=" ")
print(a.pop(2))

print("The array after poping is: ", end=" ")
for i in (a):
    print(i, end=" ")
print("\r")

#Slicing an Array
print(a[2:5])#slicing elements starting with 3 to 5
print(a[3:])#slicing from third element to the last one
print(a[::-1])#print the array in the reverse order
print(a[:3])#print elements from the 3rd to the first one

#SEARCHING AN ARRAY
#we use index() function to get the index of the first occurence of the element in the array
print("The index of the first occurence of 100 is :", end=" ")
print(a.index(400))

#UPDATING AN ARRAY
#We reasign the index with the new element we want it to hold

a[1]=700
print("The new array after updation is: ", end=" ")
for i in (a):
    print(i, end="")
print()


