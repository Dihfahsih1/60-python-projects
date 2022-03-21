import os

file = open('practicing.py')

with (open('practicing.py')) as file_read:
    for line in file_read:
        print(line)
    
    