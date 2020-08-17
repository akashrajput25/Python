print('```````````````````Welcome to guessing Game````````````````')

no = 9

count = 0
limit = 3

while count < limit:  
    x = int(input('Enter the Number'))
    count+=1
    if x == no:
        print('You won')
        break
else:
    print('You Lost')
         

    