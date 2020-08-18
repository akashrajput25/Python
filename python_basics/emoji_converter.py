message = input(">")
words = message.split(' ')
emojis ={
    ":)" : "😊",
    ":(" : "🙁",
}

convert = ""
for word in words:
    convert+= emojis.get(word , word)+" "
print(convert)