'''
for x in range(4):
    for y in range(4):
        print(f'({x} , {y})')
'''

numbers = [2 , 2 , 2 , 2 , 6 , 6]
for number in numbers:
    output = ''
    for count in range(number):
        output+= 'x'
    print(output)