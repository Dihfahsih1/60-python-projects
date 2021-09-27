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