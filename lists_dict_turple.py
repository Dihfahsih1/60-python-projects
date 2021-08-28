#list
person = ['first_name', 'age','gendar']

front_end=['html','css', 'bootstrap', 'javascript']

back_end = ['python','nodejs','java','php']

#deleting an item from a list
del front_end[1]
#print(front_end)

#concatenating lists
a,b=['aapple','mango'], [1, 2,3,4]

a=[10, 11, 12]

c = a+b
print(c)

#list compression

#using for loop
for i in c:
    if i % 2 == 0:
        #print(i) 
        pass   

#using list compression
even_numbers=[ i for i in c if i % 2 == 0]
print(even_numbers)

#using lambda expression
even_nos = list(filter(lambda x: (x % 2 == 0), c))

#buit in ATTRIBUTES of a list 
#they include all(), any(), list(), sorted(), min max sum() len()
print (even_nos, "they are " + str(len(even_numbers)) + " even numbers")
even_nos.insert(0, 64)
even_nos.append('string')

even_nos.pop()
print(max(even_nos))

print(len(even_nos))

#print(sorted(even_nos))

#Built in METHODS OF A LIST
#a function is what you apply to a construct and get a result
#A method is what you can do to it and change it
#we use a .dot operator
#they include the following append() insert() pop() remove() clear() index() count() sort() reverse()

even_nos.append('astring')

print(even_nos.index(64))

even_nos.remove('astring')

print(even_nos.sort())

print(even_nos.reverse())

#replace an item in the list
back_end[1]='django'

#append a value to the list this adds the new item to the end
back_end.append('Appended value')

#insert a value in the list at a given index
back_end.insert(2, 'Kotlin')


#back_end.extend(front_end
#print(back_end)

#del back_end[2:]

#slicing the list
back=back_end[2:5]
#print(back)

#dimensional list

a_list = [[[10, 20], 300], [400, 500], 600]
#print(a_list[0][0][0]) #print 20

test = "mugoya", "dihfahsih" "akab"
#print(list(test))

# use += operate back_end += front_end
#print(back_end)

name = 'eduraka'
name.upper()
# name[3]='t' #strings are immutable

#Dictionary
lang = {
    'py':'python',
    'js':'Javascript',
    2 : 'C++',
    3:'php'
}

#get an item from the dictionery
lang['js'] = "ReactJs"

#add a value to a dictionery
lang['ry'] = 'Ruby and Rails'
#print(lang)
#print(lang.get('js'))


#Turples
#turples are indexed, support duplicates, turples can not be assigned

a_turple = ('ug','uganda', 'tz','tanzania')
#a_turple[1] = 'adnagu'
#print(a_turple[1])

#Set
# => they can not be indexed, they have no duplicates
a_set = {12, 40, 'james', 12, 'jon', 'james'}
#print(a_set)
#print(a_set[2]) sets can not be assigned

#real world
#how can you print the first string of this (My Name Is Dihfahsih)
m='My Name is Dihfahsih'
a=[]
for i in m.split(' '):
    a.append(i[0])
print(a)
    
#test=[ i for i[0] in m.split(' ')]
# print(test)

txt = "hello, my name is Peter, I am 26 years old"
x = []
for i in txt.split("," ,2):
    x.append(i[2])

print(x)

import shutil
a ="/home/pythonista/Desktop/python/a/df.jpg"
b ="/home/pythonista/Desktop/python/b"
j= shutil.copy(a, b)



