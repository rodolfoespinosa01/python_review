# Working on Logical Operators

'''
if applicant has high income AND good credit they are Eligible for a Loan


has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
print('Eligibile for loan')


if applicant has high income OR good credit they are Eligible for a Loan


has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print('Eligibile for loan')

AND: both
OR: at least one
NOT:


if applicant has high income AND good credit they are Eligible for a Loan and doesnt have a criminal record
'''

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print('Eligibile for loan')
