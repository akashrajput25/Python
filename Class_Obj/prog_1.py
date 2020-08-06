class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('hello')

#output 10
print(Person.age)

print(Person.greet)

print(Person.__doc__)