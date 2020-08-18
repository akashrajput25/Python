'''
class Pointer:
    def __init__(self , x ,y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')

point = Pointer(10 , 20)
print(point.x + point.y)
'''

#Task_12
class Person:
    def __init__(self , name):
        self.name = name
    def talk(self):
        print(f'Hello {self.name}')


jhon = Person('Akash')
print(jhon.name)
jhon.talk()