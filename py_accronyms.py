user_text = str(input('Enter the phrase: '))

text = user_text.split()
print(text)

a = " "

for i in text:
    a = a + str(i[0]).upper()
print(a)    

