has_high_income = True
has_good_credit = True

if has_good_credit and has_high_income:
    print('Eligible for loan')

elif has_good_credit or has_high_income:
    print('Eligible for gold loan')

else:
    print('You should have an asset to take loan')


