prices = [10,45,60]

total = 0
for price in prices:
  total += price
  
print(f"Total Price: {total}")

numbers = [5, 2, 5, 2, 2 ]
# for x in numbers:
#   print('x' * x)

for x in numbers:
  output = ""
  for y in range(x):
    output += "x"
  print(output)