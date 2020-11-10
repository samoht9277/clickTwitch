import mouse

def detectPosition():
    mouse.wait(button='middle')
    pos = mouse.get_position()

    newPos = []
    for i in pos:
        newPos.append(i)

    xPos = newPos[0]
    yPos = newPos[1]

    print(xPos)
    print(yPos)
    print(xPos + yPos)

detectPosition()