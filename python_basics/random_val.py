
'''
import random
for i in range(0,1):
    print(random.randint(10,20)) 

members = ['akash' , 'singh' , 'rajput']
leader = random.choice(members)
print(leader)
'''

#Task13
import random

class Dice:
    def roll(self):
        x = random.randint(0,6)
        y = random.randint(0,6)
        return x , y

roll1 = Dice()
print(roll1.roll())