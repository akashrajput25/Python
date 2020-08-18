'''
matrix =[
    [1,2,3],
    [5,1,2],
    [9,8,3]
]

print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
'''
'''
numbers = [3,4,51,8,7,0]
numbers.append(9)
numbers.insert(0,1)
numbers.remove(51)
numbers.clear()
numbers = [3,4,51,8,7,0]
numbers_2 = numbers.copy()
numbers.pop()
print(numbers.index(4))
print(numbers.count(4))
numbers.sort()
numbers.reverse()
print(numbers_2)
print(numbers)
'''
#Task10

numbers = [23,43,23,11,45,78,43]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)