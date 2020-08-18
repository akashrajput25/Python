'''
names =['Akash' , 'Rajput' , 'Singh']
names[0] = 'DAV'
print(names[1:])
print(names[:])
'''

#Task9

numbers = [10,20,4,12,364,104,12,33,99]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(f'Largest no.in the list is {largest}')
    