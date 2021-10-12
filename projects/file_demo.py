import csv

email = ["dihfahsih.mugoya@gmail.com",'difas.mugoya@gmail.com']

for lines in email:
  line=str(lines) #convert list to string
  username = line.split("@", 1)[0]
  print(username)
  try:
    first_name = username.split('.', 1)[0].capitalize()
    print(first_name)
  except Exception as e:
    print(e)
    
  try:
    last_name = username.split('.', 1)[1].capitalize()
    print(last_name)
  except Exception as e:
    print(e)
        
    
        
  
