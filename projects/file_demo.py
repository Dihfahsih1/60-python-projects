import csv
with open("list_of_emails.csv", 'r') as data_file:
  csv_data = csv.reader(data_file)
  str1 =""
  for line in csv_data:
    print(line)
    username = str(line).split("@", 1)[0]
    print(username)
    if username.split(".", 1) == False:
      first_name = username.split('.', 1)[0].capitalize()
      print(first_name)
      last_name = username.split('.', 1)[1].capitalize()
      
    # contains = name.split(".")[0]
    # print(contains)
    # if contains:
    #   first_name = contains[0][0]
    #   print(first_name)
      
 
