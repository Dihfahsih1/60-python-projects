myvar =lambda a, b: (a+b)*2
print(myvar(2,8))

#recursion
def recusive(n):
    
    if n==1:
        return 1
    return n*recusive(n-1)

recusive(5)

#arguments
#passing keyword arguments
# def greeting(name="User", age=22):
#     print(f"Hello, {name}. You are {age} years old")
# greeting(input("Enter your name:\n"), input("Enter Your age:\n"))

#Arbitrary arguements, you literally don't know how many arguments you will be passing
def people(*names):
    for i in names:
        print(f"{i}, hello")
people('John', 'Mathew', 'Luke')

#*args in a function, pass a number of non-keyworded arguements, take in a number of more args than pre-defined

def bible(arg1, *args):
    print("the bible is all about: ", arg1)
    print("Other things the bible is all about: ", end=" ")
    for i in args:
        print(str(i),end=",")
    return 
bible('God',"creation","fall of man", 'restoration', 'judgement')

#**kwargs, this pass key-value into the function

def bible_division(*args, **kwargs):
    print(args)
    print("this is how the bible is divided up: ", end=" ")
    for key,value in kwargs.items():
        print('%s==%s' %(key, value))
bible_division(bible,old_testament="37 books",new_testament="29 books" )
        