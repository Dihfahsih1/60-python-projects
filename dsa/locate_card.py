#test=[]
test={
  'inputs':{'cards':[13,11,10,7,4,3,1,0],'query':3},
  'output':3
}
# test.append({
#   'inputs':{'cards':[13,13,9,7,4,3,2,0],'query':7}
# })
output=3
def locate_card(cards, query):
  position=0
  print('cards: ',cards)
  print('query: ',query)
  while True:
    print('position: ',position)
    if cards[position]==query:
      return position
    
    position +=1 
    
    if position == len(cards):
      return -1
    
result=locate_card(test['inputs']['cards'],test['inputs']['query'])
print(result)

if result==output:
  print('True')

#binary search function  
def binary_search(cards, query):
  lo, hi = 0,len(cards)-1
  while lo <= hi:
    mid = (lo + hi) //2
    middle_number = cards[mid]
    print('lo: ', lo, ", hi: ", hi, ', mid: ', middle_number)
    
    if middle_number==query:
      return mid
    elif middle_number<query:
      hi = mid - 1
    elif middle_number>query:
      lo = mid + 1
  return -1
result=binary_search(test['inputs']['cards'],test['inputs']['query'])
