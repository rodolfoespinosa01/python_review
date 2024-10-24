'''
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if its more than 50 characters long 
    name can be a maximum of 50 characters
otherwise
    name looks good!
'''
name = input("Please enter your name: ")
characters = len(name)

if characters < 3:
    print('name must be at least 3 characters')
elif characters > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good!')
