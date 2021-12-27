command = "" ""

while command != "quit":
  command = input("> ").lower()
  if command == "start":
    print("Car started .... ")
    
  elif command == "stop":
    print("The car stopped")
    
  elif command == "help":
    print("Start - To start Car")
    print("Stop - To stop Car")
    print("Quit - To Quit")
    
  elif command == "quit":
    break
  else:
    print("Sorry i don't understand what you are saying!!")

