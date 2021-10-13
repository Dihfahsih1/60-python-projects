import csv

email = ["dihfahsih.mugoya@gmail.com",'difasmugoya@gmail.com']

for lines in email:
  line=str(lines) #convert list to string
  #username = line.split("@", 1)[0]
  username, _, _ = line.partition("@")
  name = username.split(".")
  try:
    if len(name)>=2:
      first_name = name[0]
      print("First Name: " +first_name)
      
      last_name = name[1]
      print("Last Name :" +last_name)
      
    else:
      print(f"Your user name: {username}")
  except Exception as e:
    print('error')
    

    
        
  
