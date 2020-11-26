import subprocess
import clickTwitch
from time import sleep

# Set up.
try:
    clickInterval = int(input('Set time in seconds the mouse will click (default = 30): '))
    if clickInterval <= 1:
        raise ValueError
except ValueError:
    clickInterval = 30
finally:
    subprocess.run('cls', shell=True)
    
wantsRandom = str(input('Do you want to make a random movement every second? Y/n: '))
subprocess.run('cls', shell=True)
clickTwitch.detectPosition()

# Loops until window is closed.
while True:
    subprocess.run('cls', shell=True)
    i = 0
    clickTwitch.clickPosition(clickTwitch.detectPosition.x, clickTwitch.detectPosition.y)
    while i < clickInterval:
        sleep(1)
        i += 1
        print('%is' % i)
        if clickTwitch.isLetterY(wantsRandom):
            clickTwitch.randomMovement()
