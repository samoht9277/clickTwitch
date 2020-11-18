'''
clickTwitch is an automation tool that claims your twitch reward while watching a stream.

API:
========

`detectPosition()`

`clickPosition()`

`randomMovement()`

`isLetterY()`

'''

import mouse

def detectPosition():
    '''
    Waits until client presses middle button, then parses the mouse position to variables used by clickPosition().
    '''
    print('Position your mouse where the claiming button is. When you are ready, click the middle button on your mouse to confirm the location')
    mouse.wait(button='middle')
    pos = mouse.get_position()

    detectPosition.x = pos[0]
    detectPosition.y = pos[1]

def clickPosition(x, y):
    '''
    Moves to passed coordenates and clicks.
    '''
    mouse.move(x, y, absolute=True, duration=0.1) 
    mouse.click(button='left')

def randomMovement():
    '''
    Moves to random position.
    '''
    import random

    xRandomPosition = random.randrange(-50, 50)
    yRandomPosition = random.randrange(-50, 50)
    mouse.move(xRandomPosition, yRandomPosition, absolute=False, duration=0.1)

def isLetterY(letter):
    '''
    Returns true is parameter is a string equal to 'y'.
    '''
    if letter == 'y' or letter == 'Y':
        return True
    return False