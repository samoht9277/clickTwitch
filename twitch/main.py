import os
from time import sleep
import random
import mouse

class twitchpy:
    def click():
        mouse.move(1365, 830, absolute=True, duration=0) 
        mouse.click(button='left')
        print('clicked!')

    def randomMovement():
        xPosition = random.randrange(1260, 1599)
        yPosition = random.randrange(730, 850)
        mouse.move(xPosition, yPosition, absolute=True, duration=0.2)

# Set up.
try:
    click_interval = int(input('Set time in seconds the mouse will click (Default = 200): '))
except ValueError:
    click_interval = 200
    print('Time set to default.')
    sleep(2)

if __name__ == "__main__":
    while True:
        os.system('cls')
        twitchpy.click()
        i = 0
        while i != click_interval:
            sleep(1)
            i += 1
            print(i)
            twitchpy.randomMovement()
