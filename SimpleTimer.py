from time import sleep
from winsound import Beep
from os import system

for i in range(11):
    print(i)
    sleep(1)

Beep(500, 2000)