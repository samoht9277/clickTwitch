import mouse

class clickTwitch():
    # Waits until client pressed middle button, then parses the mouse position. 
    def detectPosition():
        print('Position your mouse where the claiming button is. When you are ready, click the middle button on your mouse to confirm the location')

        mouse.wait(button='middle')
        pos = mouse.get_position()
        newPos = []
        for i in pos:
            newPos.append(i) # Grabs tuple and appends it the value inside 'i' to an array.

        clickTwitch.detectPosition.x = newPos[0]
        clickTwitch.detectPosition.y = newPos[1]

    def clickPosition(x, y):
        mouse.move(x, y, absolute=True, duration=0) 
        mouse.click(button='left')

    def randomMovement():
        import random

        xRandomPosition = random.randrange(1260, 1599)
        yRandomPosition = random.randrange(730, 850)
        mouse.move(xRandomPosition, yRandomPosition, absolute=True, duration=0.2)