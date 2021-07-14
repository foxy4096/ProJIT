def intrest_total():
    principal = int(input("Please Enter in your balance: "))
    rate = float(input("Please Enter in your rate: "))
    number = int(input("Please Enter in how many times per year it will compounded: "))
    time= int(input("Please Enter in how many years this will comepound for: "))

    compound = 1

    while compound <= time:
        intrest_total = (principal *    ((1 + rate/ number)**(number * compound)))
        print(intrest_total)
        compound += 1
intrest_total ()