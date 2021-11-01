test=[]
test.append({
  'inputs':{'cards':[13,11,10,7,4,3,1,0],'query':7}
})
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