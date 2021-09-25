#while loop
a=3
while a>0:
    print(a)
    a-=1
    if a==1:break
else:
    print("reached 0")
  
#if we have a single statement    
a=5 
while a<0: print(a); a-=1

#using range(start,endpoint, interval)
#the range must be from less to great else the list would be empty
#the interval in the reange can also be negative(from great to less)
print("List of integers-" + str(list(range(12,2,-5))))

#iterating a list using the for loop, this can also be done on the string
list1=[1,4,6,7,10,11]
for i in list1:
    print(i)

#iterating on the indices

list2=["Holy Spirit", "God", "Jesus"]
#for loop can also have else statement after all the code inside the for loop has been executed
for i in range(len(list2)):
    print(str(i) + " " + str(list2[i]))
else:
    print("all items have been printed")
    
#Nested for loop

for i in range(0, 6):
    for j in range(i):
        print("*", end=' ')
        if i==0: break
    print()
    
#nested while loop
i=6
while(i>0):
    j=6 
    while(j>i):
        print("*", end=' ')
        j-=1
    i-=1
    print()
    
def evens(n):
    print(0)
    x=2
    for i in range(1, n):
        for j in range(i+1):
            print(x, end='')
        x*=2
        print(x)
n=int(input("how many lines?"))
evens(n)
    