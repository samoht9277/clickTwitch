import mouse

while True:
    mouse.wait(button='middle')
    pos = mouse.get_position()

    xPos = pos[2:3]
    print(xPos)