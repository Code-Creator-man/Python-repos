import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)
    return roll

deger = roll()
print(deger)