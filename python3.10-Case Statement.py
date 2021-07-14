from os import system
system("cls")
while True:
    status = int(input(">>> "))
    match status:
        case 200:
            print("OK")
        case 404:
            print("File Not Found")
        case 418:
            print("I am a Tea-Pot")
        case 500:
            print("Internal Server Error")
        case _:
            print("Something's wrong with the Internet")