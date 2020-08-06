class Parrot:
    #instance attributes
    def __init__(self , name , age):
        self.name = name
        self.age = age

    #instance method
    def sing(self , song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

#instantiate the object
blu = Parrot("Blu" , 10)

#call instance objects
print(blu.sing("happy"))
print(blu.dance())