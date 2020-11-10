import os
from time import sleep
import mouse

# Function definitions ;p
def detectPosition():
    print('Position your mouse where the claiming button is. When you are ready, click the middle button on your mouse to confirm the location')

    mouse.wait(button='middle')
    pos = mouse.get_position()
    newPos = []
    for i in pos:
        newPos.append(i) # Grabs tuple and appends it to an array.

    detectPosition.xPos = newPos[0]
    detectPosition.yPos = newPos[1]

def randomMovement():
    import random

    xRandomPosition = random.randrange(1260, 1599)
    yRandomPosition = random.randrange(730, 850)
    mouse.move(xRandomPosition, yRandomPosition, absolute=True, duration=0.2)

def clickPosition(x, y):
    mouse.move(x, y, absolute=True, duration=0) 
    mouse.click(button='left')

# Set up.
try:
    clickInterval = int(input('Set time in seconds the mouse will click (Default = 200): '))
    if clickInterval >= 1:
        print('Time setted to', clickInterval)
        sleep(1)
    else:
        raise ValueError
except ValueError:
    click_interval = 200
    print('Time set to default.')
    sleep(2)

detectPosition()

# Loop until window is closed.
if __name__ == "__main__":
    while True:
        os.system('cls') # Clear terminal.
        clickPosition(detectPosition.xPos, detectPosition.yPos)
        i = 0
        while i != clickInterval:
            sleep(1)
            i += 1
            print(str(i) + 's')
