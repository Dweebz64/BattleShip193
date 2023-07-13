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
winGame = False
moveCount = 0
hits = 0
playMsg = "Click a button!"     #Will show hit or miss at end?
pad = 10


#Clicky
def button_click(b):
    if b["text"] == "  ":
        #moveCount +=1
        if b in ship:
            b["text"]= "O"
            #hits +=1
            playMsg = "Hit!"
            checkWin()
        else:
            b["text"]= "X"
            playMsg = "Miss!"


#Will assign values for ships, find 5 random buttons
def newGame():
    pass






def checkWin():
    if hits == 5:
        winGame = True
    else:
        pass






#Define GUI Elements
frame = Frame(root)
label_a = Label(root, text="A", padx=pad)
label_b = Label(root, text="B", padx=pad)
label_c = Label(root, text="C", padx=pad)
label_d = Label(root, text="D", padx=pad)
label_e = Label(root, text="E", padx=pad)

label_1 = Label(root, text="1")
label_2 = Label(root, text="2")
label_3 = Label(root, text="3")
label_4 = Label(root, text="4")
label_5 = Label(root, text="5")

label_msg = Label(root, text= playMsg)

b1 = Button(root, text="  ", padx=10, command=lambda: button_click(b1))
b2 = Button(root, text="  ", padx=10, command=lambda: button_click(b2))
b3 = Button(root, text="  ", padx=10, command=lambda: button_click(b3))
b4 = Button(root, text="  ", padx=10, command=lambda: button_click(b4))
b5 = Button(root, text="  ", padx=10, command=lambda: button_click(b5))

b6 = Button(root, text="  ", padx=10, command=lambda: button_click(b6))
b7 = Button(root, text="  ", padx=10, command=lambda: button_click(b7))
b8 = Button(root, text="  ", padx=10, command=lambda: button_click(b8))
b9 = Button(root, text="  ", padx=10, command=lambda: button_click(b9))
b10 = Button(root, text="  ", padx=10, command=lambda: button_click(b10))

b11 = Button(root, text="  ", padx=10, command=lambda: button_click(b11))
b12 = Button(root, text="  ", padx=10, command=lambda: button_click(b12))
b13 = Button(root, text="  ", padx=10, command=lambda: button_click(b13))
b14 = Button(root, text="  ", padx=10, command=lambda: button_click(b14))
b15 = Button(root, text="  ", padx=10, command=lambda: button_click(b15))

b16 = Button(root, text="  ", padx=10, command=lambda: button_click(b16))
b17 = Button(root, text="  ", padx=10, command=lambda: button_click(b17))
b18 = Button(root, text="  ", padx=10, command=lambda: button_click(b18))
b19 = Button(root, text="  ", padx=10, command=lambda: button_click(b19))
b20 = Button(root, text="  ", padx=10, command=lambda: button_click(b20))

b21 = Button(root, text="  ", padx=10, command=lambda: button_click(b21))
b22 = Button(root, text="  ", padx=10, command=lambda: button_click(b22))
b23 = Button(root, text="  ", padx=10, command=lambda: button_click(b23))
b24 = Button(root, text="  ", padx=10, command=lambda: button_click(b24))
b25 = Button(root, text="  ", padx=10, command=lambda: button_click(b25))


ship =[b1,b2,b10]


#Display GUI Elements
frame.grid(row=0, column=0)
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

    #label_msg.grid(row=7, column=3, columnspan=2)      Needs to go into different frame container

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



root.mainloop()

