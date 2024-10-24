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
