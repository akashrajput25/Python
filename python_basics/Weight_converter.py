weight = input('Enter you weight')
type_wt = input('(L)bs or (K)g')

if type_wt.upper() == 'L':
    print(f'You are {int(weight) * 0.45} Kgs')

elif type_wt.upper() == 'K':
    print(f'You are {int(weight) * 2.216} pounds')

else:
    print('you entered incorrect')