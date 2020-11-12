import os
from time import sleep
from clickTwitch import *

# Set up.
try:
    clickInterval = int(input('Set time in seconds the mouse will click (Default = 200): '))
    if clickInterval >= 1:
        print('Time setted to', clickInterval)
        sleep(1)
    else:
        raise ValueError
except ValueError:
    clickInterval = 200
    print('Time set to default.')
    sleep(2)

clickTwitch.detectPosition()

# Loop until window is closed.
while True:
    os.system('cls') # Clear terminal.
    clickTwitch.clickPosition(clickTwitch.detectPosition.x, clickTwitch.detectPosition.y) # Disgusting parameter passing.
    i = 0
    while i != clickInterval:
        sleep(1)
        i += 1
        print(str(i) + 's')