import os 
from clickTwitch import *
from time import sleep

# Set up.
try:
    clickInterval = int(input('Set time in seconds the mouse will click (default = 200): '))
    if clickInterval < 1:
        raise ValueError
except ValueError:
    clickInterval = 200
finally:
    os.system('cls')
    
wantsRandom = str(input('Do you want to make a random movement every second? Y/n: '))
os.system('cls')
clickTwitch.detectPosition()

# Loops until window is closed.
while True:
    os.system('cls')
    i = 0
    clickTwitch.clickPosition(clickTwitch.detectPosition.x, clickTwitch.detectPosition.y)
    while i < clickInterval:
        sleep(1)
        i += 1
        print('%ss' % i)
        if clickTwitch.isLetterY(wantsRandom):
            clickTwitch.randomMovement()
