user_text = str(input('Enter the phrase: '))
print(user_text)
text = user_text.split() #split the setence into separate strings
print(text)

a = " " #defining the variable that would store our first letter of the word

for i in text: #loop through the splitted text
    a = a + str(i[0]).upper()#store each first letter of the splitted text and convert it to upper case
print(a)    

