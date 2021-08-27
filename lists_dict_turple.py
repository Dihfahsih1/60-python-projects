#list
person = ['first_name', 'age','gendar']

front_end=['html','css', 'bootstrap', 'javascript']

back_end = ['python','nodejs','java','php']

#replace an item in the list
back_end[1]='django'

#append a value to the list
back_end.append('Appended value')

#insert a value in the list at a given index
back_end.insert(2, 'Kotlin')


#back_end.extend(front_end
print(back_end)

#del back_end[2:]

#slicing the list
back=back_end[2:5]
print(back)

#dimensional list

a_list = [[[10, 20], 300], [400, 500], 600]
print(a_list[0][0][0]) #print 20

test = "mugoya", "dihfahsih" "akab"
print(list(test))

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
print(lang)
#print(lang.get('js'))


#Turples
#turples are indexed, support duplicates, turples can not be assigned

a_turple = ('ug','uganda', 'tz','tanzania')
#a_turple[1] = 'adnagu'
print(a_turple[1])

#Set
# => they can not be index, they have no duplicates
a_set = {12, 40, 'james', 12, 'jon', 'james'}
print(a_set)
#print(a_set[2]) sets can not be assigned
  
