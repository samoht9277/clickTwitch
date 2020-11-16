import mouse

class clickTwitch():

    def detectPosition():
        '''
        Waits until client presses middle button, then parses the mouse position to variables used by clickPosition().
        '''
        print('Position your mouse where the claiming button is. When you are ready, click the middle button on your mouse to confirm the location')

        mouse.wait(button='middle')
        pos = mouse.get_position()
        newPos = []
        for i in pos:
            newPos.append(i) # Grabs tuple and appends it the value inside 'i' to an array.

        clickTwitch.detectPosition.x = newPos[0]
        clickTwitch.detectPosition.y = newPos[1]

    def clickPosition(x, y):
        '''
        Moves to passed coordenate and clicks.
        '''
        mouse.move(x, y, absolute=True, duration=0) 
        mouse.click(button='left')

    def randomMovement():
        '''
        Moves to random position, to prevent twitch from detecting the clicker.
        '''
        import random

        xRandomPosition = random.randrange(-50, 50)
        yRandomPosition = random.randrange(-50, 50)
        mouse.move(xRandomPosition, yRandomPosition, absolute=False, duration=0.1)

    def isLetterY(wantsRandom):
        '''
        Returns true is wantsRandom is equal to 'y' (yes).
        '''
        if wantsRandom == 'y' or wantsRandom == 'Y':
            return True
        return False
