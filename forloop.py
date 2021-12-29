prices = [10,45,60]

total = 0
for price in prices:
  total += price
  
print(f"Total Price: {total}")

for x in range(5):
  for y in range(5):
    print(f"({x}, {y})")