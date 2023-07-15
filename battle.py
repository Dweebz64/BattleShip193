"""
Battleship 193

This program generates a Tkinter GUI grid to play a game of Battleship with the user.

By CWhite and TiaFields.

"""

import random
from tkinter import *


root = Tk()
root.title("BattleShip 193")
root.geometry("320x350")


#Varibles
pad = 10
playMsg = StringVar()
moveMsg = StringVar()


#Clicky
def button_click(b):
    global moveCount, hits, playMsg
    
    if b["text"] == "  ":
        moveCount +=1
        moveMsg.set("Moves: " + str(moveCount))
        if b in ships:
            b["text"]= "O"
            hits +=1
            playMsg.set("Hit!")
            checkWin()
        else:
            b["text"]= "X"
            playMsg.set("Miss!")


#Will assign values for ships, find 5 random buttons
def newGame():
    global winGame, moveCount, hits, playMsg, ships

    winGame = False
    moveCount = 0
    hits = 0
    playMsg.set("Click a button to play!")
    moveMsg.set("Moves: " + str(moveCount))
    spaces = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]
    ships = random.sample(spaces, 5)

    


def checkWin():
    if hits == 5:
        winGame = True
    else:
        pass






#Define GUI Elements
board_frame = LabelFrame(root, text="Battleship 193")
label_a = Label(board_frame, text="A", padx=pad)
label_b = Label(board_frame, text="B", padx=pad)
label_c = Label(board_frame, text="C", padx=pad)
label_d = Label(board_frame, text="D", padx=pad)
label_e = Label(board_frame, text="E", padx=pad)

label_1 = Label(board_frame, text="1")
label_2 = Label(board_frame, text="2")
label_3 = Label(board_frame, text="3")
label_4 = Label(board_frame, text="4")
label_5 = Label(board_frame, text="5")

b1 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b1))
b2 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b2))
b3 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b3))
b4 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b4))
b5 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b5))

b6 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b6))
b7 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b7))
b8 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b8))
b9 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b9))
b10 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b10))

b11 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b11))
b12 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b12))
b13 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b13))
b14 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b14))
b15 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b15))

b16 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b16))
b17 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b17))
b18 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b18))
b19 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b19))
b20 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b20))

b21 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b21))
b22 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b22))
b23 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b23))
b24 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b24))
b25 = Button(board_frame, text="  ", padx=10, command=lambda: button_click(b25))


msg_frame = Frame(root)
label_msg = Label(msg_frame, textvariable=playMsg)
moves_msg = Label(msg_frame, textvariable=moveMsg)


#Display GUI Elements
board_frame.grid(row=0, column=0)
label_a.grid(row=1, column=1)
label_b.grid(row=1, column=2)
label_c.grid(row=1, column=3)
label_d.grid(row=1, column=4)
label_e.grid(row=1, column=5)

label_1.grid(row=2, column=0)
label_2.grid(row=3, column=0)
label_3.grid(row=4, column=0)
label_4.grid(row=5, column=0)
label_5.grid(row=6, column=0)

b1.grid(row=2, column=1)
b2.grid(row=2, column=2)
b3.grid(row=2, column=3)
b4.grid(row=2, column=4)
b5.grid(row=2, column=5)

b6.grid(row=3, column=1)
b7.grid(row=3, column=2)
b8.grid(row=3, column=3)
b9.grid(row=3, column=4)
b10.grid(row=3, column=5)

b11.grid(row=4, column=1)
b12.grid(row=4, column=2)
b13.grid(row=4, column=3)
b14.grid(row=4, column=4)
b15.grid(row=4, column=5)

b16.grid(row=5, column=1)
b17.grid(row=5, column=2)
b18.grid(row=5, column=3)
b19.grid(row=5, column=4)
b20.grid(row=5, column=5)

b21.grid(row=6, column=1)
b22.grid(row=6, column=2)
b23.grid(row=6, column=3)
b24.grid(row=6, column=4)
b25.grid(row=6, column=5)

msg_frame.grid(row=7, column=0)
label_msg.grid(row=8, column=0)
moves_msg.grid(row=9, column=0)


newGame()
root.mainloop()


