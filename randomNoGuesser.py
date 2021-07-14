# Importing the random to generate random no.
import random
print("""Number Guesser game""")
# Setting the random no.
no = random.randrange(0, 10)
count = 5
while count > 0:
    g = input("Please Input the no >>> ")
    g = int(g)
    if g < no:
        print("The no. is less")
        count = count-1
    elif g > no:
        print("The no. is more")
        count = count-1
    elif g == no:
        print(f"You are correct, the no. is {no}")
        break
if count == 0:
    print("You Lose")