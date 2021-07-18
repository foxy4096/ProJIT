class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def save(self):
        data = {
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
        with open('data.txt', mode='r+') as file:
            temp_data = file.read()
            file.write(str(data) + '\n' + temp_data)
            file.close()
            print("Data Written Successfully")

    def delete(self):
        data = {
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
        with open('data.txt', mode='r+') as file:
            for person in file.read():
                if person == str(data):
                    person = ''
            file.close()
            print("Data Removed Successfully")

    @staticmethod
    def show():
        persons = []
        with open('data.txt', mode='r+') as file:
            for person in file.read():
                persons.append(dict(person))
            file.close
        return persons


aditya = Person("Aditya", 16, "M")
aditya.save()