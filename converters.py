prices = [10,45,60]

total = 0
for price in prices:
  total += price
  
print(f"Total Price: {total}")

numbers = [1,3,6,8,9,10,5,2 ]
# for x in numbers:
#   print('x' * x)

for x in numbers:
  output = ""
  for y in range(x):
    output += "x"
  print(output)
  
#printing the largest number  
class find_max(number):
  max = number[0]
  for num in number:
    if num > max:
      max = num
  print(max)
find_max()
  