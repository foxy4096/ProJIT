print("Type exit to exit")
while True:
    try:
        a = input(">>> ")
        if a.lower() == "exit":
            break
        elif "import" in a.lower():
            print("Do you want want to brick you computer you dumb monke")
        result = eval(a)
        print(f"The result is: {result}")
    except Exception as e:
        print("You Idiot you need to sepcify the number as 123 not as one, two three")
        print(e)

