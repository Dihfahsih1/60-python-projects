command = "" ""
started = False
while True:
  command = input("> ").lower()
  if command == "start":
    if started:
      print("the car already started..")
      
    else:
      started = True
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

