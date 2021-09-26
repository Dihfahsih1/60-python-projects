myvar =lambda a, b: (a+b)*2
print(myvar(2,8))

#recursion
def recusive(n):
    
    if n==1:
        return 1
    return n*recusive(n-1)

recusive(5)