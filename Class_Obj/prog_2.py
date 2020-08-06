class Person:
    "This is person class"
    age = 10

    def greet(self):
        print('hello')

#create a new object of person class
harry = Person()

print(Person.greet)

print(harry.greet)

harry.greet()