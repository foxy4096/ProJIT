from datetime import date
from enum import Flag, auto

class Weekday(Flag):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

    @classmethod
    def from_date(cls, date):
        return str(cls(date.isoweekday())).title()


for day in Weekday:
    print(day)

chores_for_ethan = {
     'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
     'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
     'answer 50 questions': Weekday.SATURDAY,
     }

def show_chores(chores, day):
     for chore, days in chores.items():
         if day in days:
             print(chore)

for day in Weekday:
    show_chores(chores_for_ethan, day)