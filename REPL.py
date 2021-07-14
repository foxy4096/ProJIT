print('''Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.''')
while True:
    try:
        a = input(">>> ")
        if a.lower() == "exit":
            break
        elif a.lower() == "fun":
            import antigravity
        z = eval(a)
        print(z)
    except Exception as e:
        print("You Idiot, you donkey")
        print(e)

