def linear_search(numbers_list, number_to_find):
  for index, element in enumerate(numbers_list):
    if element == number_to_find:
      return index 
  return -1

def binary_search(numbers_list,number_to_find):
  pass

if __name__ == '__main__':
  numbers_list = [12,13,14,17,25,45,78]
  number_to_find = int(input('Please enter the number to find: '))
  
  
  index = linear_search(numbers_list,number_to_find)
  print(f'number found at index {index} using linear search')