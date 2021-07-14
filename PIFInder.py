import math 

def CalculatePi(roundVal):

		somepi = round(math.pi,roundVal)
		pi = str(somepi)
		someList = list(pi)
		return somepi
roundTo = input('Enter the number of digits you want after the decimal for Pi: ')
try:
	roundint = int(roundTo)
	print(CalculatePi(roundint))
except:
	print("You did not enter an integer")