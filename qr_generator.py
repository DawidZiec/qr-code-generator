# A little script that creates random QR codes every .75 second
# One block 20px - whole thing 540

import tkinter
from random import randint
from time import sleep

# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root, bg="white", height=540, width=540)

# enable rgb in tkinter
def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code"""
    return "#%02x%02x%02x" % rgb

while True:
    ############## LOOPING PART WITH RANDOM CODES ##############
    for t in range(0, 25):
        for u in range(0, 25):
            coord = 20+(t*20), 20+(u*20), 40+(t*20), 40+(u*20)
            ab = randint(0, 1)
            if ab == 1:
                square = myCanvas.create_rectangle(coord, fill="black", outline="black")

    # coords = x1, y1, x2, y2
    # big squares
    coordcorner = 20, 20, 160, 160
    squarecorner = myCanvas.create_rectangle(coordcorner, fill="black", outline="black")
    coordcorner2 = 380, 20, 520, 160
    squarecorner2 = myCanvas.create_rectangle(coordcorner2, fill="black", outline="black")
    coordcorner3 = 20, 380, 160, 520
    squarecorner3 = myCanvas.create_rectangle(coordcorner3, fill="black", outline="black")
    
    # top left filling
    coordcorner4 = 40, 40, 140, 140
    squarecorner4 = myCanvas.create_rectangle(coordcorner4, fill="white", outline="white")
    coordcorner5 = 60, 60, 120, 120
    squarecorner5 = myCanvas.create_rectangle(coordcorner5, fill="black", outline="black")
    
    # top right filling
    coordcorner6 = 400, 40, 500, 140
    squarecorner6 = myCanvas.create_rectangle(coordcorner6, fill="white", outline="white")
    coordcorner7 = 420, 60, 480, 120
    squarecorner7 = myCanvas.create_rectangle(coordcorner7, fill="black", outline="black")
    
    # bottom left filling
    coordcorner8 = 40, 400, 140, 500
    squarecorner8 = myCanvas.create_rectangle(coordcorner8, fill="white", outline="white")
    coordcorner9 = 60, 420, 120, 480
    squarecorner9 = myCanvas.create_rectangle(coordcorner9, fill="black", outline="black")

    # edges of the big squares

    # top left
    # vertical
    coordcorner10 = 160, 20, 180, 180
    squarecorner10 = myCanvas.create_rectangle(coordcorner10, fill="white", outline="white")
    # horizontal
    coordcorner11 = 20, 160, 180, 180
    squarecorner11 = myCanvas.create_rectangle(coordcorner11, fill="white", outline="white")

    # top right
    # vertical
    coordcorner10 = 360, 20, 380, 180
    squarecorner10 = myCanvas.create_rectangle(coordcorner10, fill="white", outline="white")
    # horizontal
    coordcorner11 = 360, 160, 520, 180
    squarecorner11 = myCanvas.create_rectangle(coordcorner11, fill="white", outline="white")

    # bottom left
    # vertical
    coordcorner10 = 160, 360, 180, 520
    squarecorner10 = myCanvas.create_rectangle(coordcorner10, fill="white", outline="white")
    # horizontal
    coordcorner11 = 20, 360, 180, 380
    squarecorner11 = myCanvas.create_rectangle(coordcorner11, fill="white", outline="white")
    
    # drawing
    myCanvas.pack()
    root.update()
    sleep(.75)
    myCanvas.delete("all")
