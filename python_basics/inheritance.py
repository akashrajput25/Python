class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('bark')

class Cat(Mammal):
    def annoying(self):
        print('annoying')

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.annoying()