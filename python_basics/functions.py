'''
def greet_user(user , company):
    print(f'Hii {user}')
    print(f'We are glad to know that you are from {company}')

#positional arguments
print('start')
greet_user('Akash','IBM')
greet_user('Rajput','Google')
print('over')

#keyword arguments
print('start')
greet_user(user = 'Akash', company = 'IBM')
greet_user(user = 'Rajput' , company = 'Google')
print('over')
'''
message = input(">")
def emojis(message):

    words = message.split(' ')
    emojis ={
        ":)" : "😊",
        ":(" : "🙁",
    }

    convert = ""
    for word in words:
        convert+= emojis.get(word , word)+" "
    return convert


print(emojis(message))