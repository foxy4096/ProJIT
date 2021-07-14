import keyboard as kb
import random
from os import system

def clearScreen():
    """Clear the Terminal"""
    system('cls')

clearScreen()

print("""
Rock, Paper, Scissors Game
By: Aditya Priyadarshi 💻 (Foxy4096) 🦊
""")

def computerSelector():
    """Randomly return the option R, P, S"""
    random_no =  random.randrange(1, 4)
    computer = None
    if random_no == 1:
        computer = 'R'
    elif random_no == 2:
        computer = 'P'
    elif random_no == 3:
        computer = 'S'
    return computer

running = True
def game(running:bool, computer_input:str):
    while running:
        choose_list = ['R', 'P', 'S']
        print("Press 'R' for Rock, 'P' for Paper or 'S' for Scissors or 'Q' to quit")
        
        # This option uses the keyboard module
        # print("Enter Your Option ➡")
        # user_input = str(kb.read_key()).upper()

        # This option uses the default input() function
        user_input = input("Enter Your Option ➡ ").upper()
        if user_input in choose_list:
            running = False
        elif user_input == 'Q':
            clearScreen()
            exit()
        else:
            print("Incorrect Option")
            clearScreen()
        print(f"You Choose for '{user_input}'")
        print(f"Computer Choose for '{computer_input}'")
        if computer_input == user_input:
            print("Tie 💻/🧑")
            running = False
        elif computer_input == 'R' and user_input == 'S' or computer_input == 'P' and user_input == 'R' or computer_input == 'S' and user_input == 'P':
            print("The Computer Won 💻 🎉")
        elif computer_input == 'R' and user_input == 'P' or computer_input == 'P' and user_input == 'S' or computer_input == 'S' and user_input == 'R':
            print("The User Won 🧑 🎉")


game(running, computerSelector())


