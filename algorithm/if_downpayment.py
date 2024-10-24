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