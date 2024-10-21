'''
if its a hot
    its a hot day
    drink plenty of water
otherwise if its cold
    its a cold day
    wear warm clothes
otherwise
    its a lovely day
'''

# code the above using if statement


'''
x = input()  # x represents the weather

if int(x) > 80:
    print('its a hot day')
    print('drink plenty of water')
elif int(x) < 60:
    print('its a cold day')
    print('wear warm clothes')
else:
    print('its a loveley day')
'''
'''
is_hot = False
is_cold = False

if is_hot:
    print('its a hot day')
    print('drink plenty of water')
elif is_cold:
    print('its a cold day')
    print('wear warm clothes')
else:
    print('its a loveley day')
'''
# Assignment
'''
Price of a house is $1M
If buyer has good credit
    they need to put down 10%
Otherwise
    they need to put down 20%
Print the down payment
'''

has_good_credit = False
price = 1000000
good_credit_downpayment = .1
bad_credit_downpayment = .2

if has_good_credit:
    down_payment = .1 * price
else:
    down_payment = .2 * price
print(f"Down payment: ${down_payment}")
