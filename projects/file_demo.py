import csv

#email = ["dihfahsih.mugoya@gmail.com",'difasmugoya@gmail.com']
with open('list_of_emails.csv', 'r') as f:
  email = csv.reader(f)
  new_list=[]
  for lines in email:
    line=str(lines) #convert list to string
    #username = line.split("@", 1)[0]
    username, _, _ = line.partition("@")
    name = username.split(".")
    try:
      if len(name)>=2:
        first_name = name[0]
        new_list.append(first_name)
        #print("First Name: " +first_name)
        
        last_name = name[1]
        #print("Last Name :" +last_name)
        new_list.append(last_name)
        
      else:
        print(f"Your username is  {username}")
    except Exception as e:
      print('error')
  print(new_list)
      
      

    
        
  
