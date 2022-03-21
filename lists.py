matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for row in matrix:
  for item in row:
    print(item)


numbers = [20, 40, 10, 4, 70]
numbers.insert(0,30)
numbers.append(100)
numbers.sort()
numbers.reverse()
numbers.pop()
numbers.remove(40)
print(numbers)


#remove duplicates
repeated_number= [10,1,10,20,30,40,50,10,30]
uniques=[]
for num in repeated_number:
  if num not in uniques:
    uniques.append(num)
print(uniques)    
    