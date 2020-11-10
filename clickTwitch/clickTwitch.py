import os
from time import sleep
import random
import mouse

# Function declaration ;p
def clickPosition(xPosition, yPosition):
    mouse.move(xPosition, yPosition, absolute=True, duration=0) 
    mouse.click(button='left')

def randomMovement():
    xRandomPosition = random.randrange(1260, 1599)
    yRandomPosition = random.randrange(730, 850)
    mouse.move(xRandomPosition, yRandomPosition, absolute=True, duration=0.2)
    

# Set up.
try:
    clickInterval = int(input('Set time in seconds the mouse will click (Default = 200): '))
except ValueError:
    click_interval = 200
    print('Time set to default.')
    sleep(2)

# Loop until exited. (pressed 'x')
if __name__ == "__main__":
    while True:
        os.system('cls') # Clear terminal.
        clickPosition(1365, 830) # Pass x and y as a parameter that defines where the claim button is.
        i = 0
        while i != clickInterval:
            sleep(1)
            i += 1
            print(str(i) + 's')
            randomMovement()
