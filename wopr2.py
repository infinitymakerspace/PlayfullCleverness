import sys
from os import system

from time import sleep

system('cls')
words = "GREETINGS PROFESSOR FALKEN \n"  "WOULD YOU LIKE TO PLAY A GAME \n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
    