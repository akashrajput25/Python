'''
customer = {
    "name" : "Akash",
    "age" : 20,
    "is_verified": True
}
customer["name"] = "Rajput"

print(customer["name"])
print(customer.get("birthday")) #returns boolean
'''
#Task10
numbers = input('Phone: ')
'''
for number in numbers:
    if number == '1':
        print('One', end=" ")
    if number == '2':
        print('Two', end =" ")
    if number == '3':
        print('Three', end=" ")
    if number == '4':
        print('Four', end=" ")
    if number == '5':
        print('Five', end=" ")
    if number == '6':
        print('Six', end=" ")
    if number == '7':
        print('Seven', end=" ")
    if number == '8':
        print('Eight', end=" ")
    if number == '9':
        print('Nine', end=" ")
    if number == '0':
        print('Zero', end=" ")
    '''
digit_dict ={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
output = ""
for number in numbers:
    output+=digit_dict.get(number,"!")+ " "

print(output)