import os, random, time

colors = 'RGBY'
guess_seq =''
#guess_time=input("Enter either of these memory times: 1 or 1.5 or 2 :- \n")
for score in range(0,10):
  guess_seq += random.choice(colors)
  for color in guess_seq:
    print(color)
    time.sleep(1.5)
    os.system('clear')
  guess = input("Repeat: ")
  os.system("clear")
  if guess != guess_seq:
    break
print(f"Game Over!, Your final score is: {score}")
  