# Give Some Dummy data
data = input("Please Type Something\n➡ ")
# Opening the file
file = open(file="data", mode='r+')
# Writing the file
file.write(str(data))
# Printing the contents of the file
print(file.read())
# Closing the file
file.close()
# Ok Now I am getting really mad
