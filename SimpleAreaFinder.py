# Importing math module for Sqroot and Pi.
import math

#This is the menu part.
menu = """
A SIMPLE AREA FINDER FOR BASIC SHAPER.
1. For Circle
2. For Square
3. For Triangle
"""

# This prints the menu
print(menu) 

# Getting the option input 
Is_Option_Selected = False
while not Is_Option_Selected:
    try:
        option = int(input("Please select the option "))
        if option > 0 and option < 4:
            Is_Option_Selected = True
        else:
            print("Please Select From the list.")
            Is_Option_Selected = False
    except:
        print("Must be a number")
        Is_Option_Selected = False

# This is the processing part
def Asker(option):
    if option == 1:
        Circle()
    elif option == 2:
        Square()
    elif option == 3:
        Triangle()
# Circle
def Circle():
    Is_End = False
    while not Is_End:
        radius = input("Please Enter the Radius >>> ")
        try:
            r = int(radius)
            area = 2 * math.pi * r
            return print(f"The Area of the Circle is {area} or ~ {round(area)} units")
            Is_End = True
        except:
            print("Must Be a Number")
            Is_End = False

def Square():
    Is_End = False
    while not Is_End:
        side = input("Please Enter the Side >>> ")
        try:
            s = int(side)
            area = s*s
            return print(f"The Area of the Square is {area} units")
            Is_End = True
        except:
            print("Must be a Number")
            Is_End = False

def Triangle():
    Is_End_1 = False
    while not Is_End_1:
        type_menu = """
Please enter the type of Triangle (In number):

1. A Triangle given Sides a, b, c
2. A Triangle given it's Height and Base
3. An equal-sides Triangle
        """
        print(type_menu)
        try:
            Stype = int(input("Please Enter the type >>> "))
            Is_End_1 = true
        except:
            print("Option Must be a number")
            Is_End_1 = False



    def ABC():
        a = input("Please input the First Side >>> ")
        b = input("Please input the Second Side >>> ")
        c = input("Please input the Third Side >>> ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            s = (a+b+c)/2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return print(f"The area of the triangle is {area} or ~ {round(area)}")
        except:
            print("lol")
            
            
            
            if Stype == 1:
                ABC()
Asker(option)