data = {
    'Book': "Two Scoops of Django",
    'Version': "3.2"
}

with open('data.txt', mode='r+') as file:
    data_temp = file.read()
    print(file.read())
    file.write(str(data + '\n'))
    print(file.read())
    file.close()
