#parent class
class Bird:
    def __init__(self):
        print('Bird ready')

    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

#child class
class Penguin(Bird):
    def __init__(self):

        #call super function
        super().__init__()
        print('penguin is ready')

    def whoisthis(self):
        print('penguin')

    def run(self):
        print("run faster")

peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()