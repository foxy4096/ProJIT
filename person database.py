# Create A database for person

import sqlite3

conn = sqlite3.connect('person.db')
c = conn.cursor("""CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    greetings INTEGER DEFAULT 0,
    friends INTEGER DEFAULT 0
);
""")


# A simple Person Class


class Person:
    """
    A Class for Person
    """
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

        c.conn.execute("""
        INSERT INTO person (name, email, phone)
        VALUES (?, ?, ?)
        """, (self.name, self.email, self.phone))
        conn.commit()

    def __repr__(self):
        return f'{self.name} (email: {self.email}, phone: {self.phone})'

    def greet(self, other_person):
        self.greeting_count += 1
        print(f'Hello {other_person.name}, I am {self.name}!')
        other_person.greeting_count += 1

    def print_contact_info(self):
        print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

    def __str__(self):
        return f'{self.name} (email: {self.email}, phone: {self.phone})'

    def __repr__(self) -> str:
        return f'{self.name} (email: {self.email}, phone: {self.phone})'

def menu():
    """
    Prints the menu
    """
    print('Menu:')
    print('1 - Add a person')
    print('2 - Print a person')
    print('3 - Print number of people')
    print('4 - Greet a person')
    print('5 - Print number of greetings')
    print('6 - Add a friend')
    print('7 - Print number of friends')
    print('8 - Exit')

options = ['1', '2', '3', '4', '5', '6', '7', '8']
menu()
input_option = input('Enter an option: ')

if input_option not in options:
    print('Invalid option')
    exit()

else:
    if input_option == '1':
        name = input('Enter name: ')
        email = input('Enter email: ')
        phone = input('Enter phone: ')
        person = Person(name, email, phone)
        print(person)