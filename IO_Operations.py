# Give Some Dummy data
data = input("Please Type Something\n➡ ")
# Opening the file
with open(file="data", mode='r+') as file:
    # Writing the file
    file.write(str(data))
    # Printing the contents of the file
    print(file.read())
    # Closing the file
    # Ok Now I am getting really mad
