import random

def computerSelector():
    random_no =  random.randrange(1, 4)
    computer = None
    if random_no == 1:
        computer = 'R'
    elif random_no == 2:
        computer = 'P'
    elif random_no == 3:
        computer = 'S'
    return computer, random_no

print(computerSelector())