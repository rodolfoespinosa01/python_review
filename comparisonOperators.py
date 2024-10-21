# using comparison operators
'''
temperature = 35

if temperature > 30:
    print('its a hot day')
else:
    print('it not a hotday')
'''


'''
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if its more than 50 characters long 
    name can be a maximum of 50 characters
otherwise
    name looks good!
'''
'''
name = input("Please enter your name: ")
characters = len(name)

if characters < 3:
    print('name must be at least 3 characters')
elif characters > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good!')
'''

# Assignment - Allow user to enter their weight, then ask if its kg or lbs,
# then show weight in lbs, if entered in lbs then show kg

weight = input('Enter your weight: ')
measurement = input('(L)bs or (K)g: ')

if measurement.lower() == 'l':
    new_weight = int(weight) * .45
    print(f"You are {new_weight} kg")
elif measurement.lower() == 'k':
    new_weight = int(weight) * 2.2
    print(f"You are {new_weight} lbs")
else:
    print('invalid measurement')
