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

"""
#Ship assignment idea
#SHIP NUMBERS
aircraftCarrier = [0,0,0,0,0]
battleship = [0,0,0,0]
cruiser = [0,0,0,0]
submarine = [0,0,0]
destroyer = [0,0]
#Length of ship
l = 5

#Places ships, ensures that they fit on the board
def placeShips()

positions = ["horizontal","vertical"]
#determines head of ship, x = head
	currentPosition = random.choice(positions)
	if currentPosition = "vertical"
		x = random.choice([1,(100-l*10)])
		ship = [x,x+10,x+20,x+30,x+40]
	if 	currentPosition = "horizontal"			#Needless words for planning logic, change to else before publish
		a = random.choice([1,9])
		b = random.choice([1,10-l])
		x = a*10 + b
		ship = [x,x+1,x+2,x+3,x+4]				#Needs to be loop to populate list

"""

#Checks button function
def button_click(b):
	b["text"] = "X"


"""

	if button_numPressed text  != " "
		ignore
	else
		if numPressed in ship numbers
			text = "O"
			msg = "Hit!"
		else
			text = "X"
			msg = "Miss"



"""




#Define Buttons
button_1 = Button(root, text=" ", padx=10, command=lambda: button_click(1))
button_2 = Button(root, text=" ", padx=10, command=lambda: button_click(2))
button_3 = Button(root, text=" ", padx=10, command=lambda: button_click(3))
button_4 = Button(root, text=" ", padx=10, command=lambda: button_click(4))
button_5 = Button(root, text=" ", padx=10, command=lambda: button_click(5))
button_6 = Button(root, text=" ", padx=10, command=lambda: button_click(6))
button_7 = Button(root, text=" ", padx=10, command=lambda: button_click(7))
button_8 = Button(root, text=" ", padx=10, command=lambda: button_click(8))
button_9 = Button(root, text=" ", padx=10, command=lambda: button_click(9))
button_10 = Button(root, text=" ", padx=10, command=lambda: button_click(10))

button_11 = Button(root, text=" ", padx=10, command=lambda: button_click(11))
button_12 = Button(root, text=" ", padx=10, command=lambda: button_click(12))
button_13 = Button(root, text=" ", padx=10, command=lambda: button_click(13))
button_14 = Button(root, text=" ", padx=10, command=lambda: button_click(14))
button_15 = Button(root, text=" ", padx=10, command=lambda: button_click(15))
button_16 = Button(root, text=" ", padx=10, command=lambda: button_click(16))
button_17 = Button(root, text=" ", padx=10, command=lambda: button_click(17))
button_18 = Button(root, text=" ", padx=10, command=lambda: button_click(18))
button_19 = Button(root, text=" ", padx=10, command=lambda: button_click(19))
button_20 = Button(root, text=" ", padx=10, command=lambda: button_click(20))

button_21 = Button(root, text=" ", padx=10, command=lambda: button_click(21))
button_22 = Button(root, text=" ", padx=10, command=lambda: button_click(22))
button_23 = Button(root, text=" ", padx=10, command=lambda: button_click(23))
button_24 = Button(root, text=" ", padx=10, command=lambda: button_click(24))
button_25 = Button(root, text=" ", padx=10, command=lambda: button_click(25))
button_26 = Button(root, text=" ", padx=10, command=lambda: button_click(26))
button_27 = Button(root, text=" ", padx=10, command=lambda: button_click(27))
button_28 = Button(root, text=" ", padx=10, command=lambda: button_click(28))
button_29 = Button(root, text=" ", padx=10, command=lambda: button_click(29))
button_30 = Button(root, text=" ", padx=10, command=lambda: button_click(30))

button_31 = Button(root, text=" ", padx=10, command=lambda: button_click(31))
button_32 = Button(root, text=" ", padx=10, command=lambda: button_click(32))
button_33 = Button(root, text=" ", padx=10, command=lambda: button_click(33))
button_34 = Button(root, text=" ", padx=10, command=lambda: button_click(34))
button_35 = Button(root, text=" ", padx=10, command=lambda: button_click(35))
button_36 = Button(root, text=" ", padx=10, command=lambda: button_click(36))
button_37 = Button(root, text=" ", padx=10, command=lambda: button_click(37))
button_38 = Button(root, text=" ", padx=10, command=lambda: button_click(38))
button_39 = Button(root, text=" ", padx=10, command=lambda: button_click(39))
button_40 = Button(root, text=" ", padx=10, command=lambda: button_click(40))

button_41 = Button(root, text=" ", padx=10, command=lambda: button_click(41))
button_42 = Button(root, text=" ", padx=10, command=lambda: button_click(42))
button_43 = Button(root, text=" ", padx=10, command=lambda: button_click(43))
button_44 = Button(root, text=" ", padx=10, command=lambda: button_click(44))
button_45 = Button(root, text=" ", padx=10, command=lambda: button_click(45))
button_46 = Button(root, text=" ", padx=10, command=lambda: button_click(46))
button_47 = Button(root, text=" ", padx=10, command=lambda: button_click(47))
button_48 = Button(root, text=" ", padx=10, command=lambda: button_click(48))
button_49 = Button(root, text=" ", padx=10, command=lambda: button_click(49))
button_50 = Button(root, text=" ", padx=10, command=lambda: button_click(50))

button_51 = Button(root, text=" ", padx=10, command=lambda: button_click(51))
button_52 = Button(root, text=" ", padx=10, command=lambda: button_click(52))
button_53 = Button(root, text=" ", padx=10, command=lambda: button_click(53))
button_54 = Button(root, text=" ", padx=10, command=lambda: button_click(54))
button_55 = Button(root, text=" ", padx=10, command=lambda: button_click(55))
button_56 = Button(root, text=" ", padx=10, command=lambda: button_click(56))
button_57 = Button(root, text=" ", padx=10, command=lambda: button_click(57))
button_58 = Button(root, text=" ", padx=10, command=lambda: button_click(58))
button_59 = Button(root, text=" ", padx=10, command=lambda: button_click(59))
button_60 = Button(root, text=" ", padx=10, command=lambda: button_click(60))

button_61 = Button(root, text=" ", padx=10, command=lambda: button_click(61))
button_62 = Button(root, text=" ", padx=10, command=lambda: button_click(62))
button_63 = Button(root, text=" ", padx=10, command=lambda: button_click(63))
button_64 = Button(root, text=" ", padx=10, command=lambda: button_click(64))
button_65 = Button(root, text=" ", padx=10, command=lambda: button_click(65))
button_66 = Button(root, text=" ", padx=10, command=lambda: button_click(66))
button_67 = Button(root, text=" ", padx=10, command=lambda: button_click(67))
button_68 = Button(root, text=" ", padx=10, command=lambda: button_click(68))
button_69 = Button(root, text=" ", padx=10, command=lambda: button_click(69))
button_70 = Button(root, text=" ", padx=10, command=lambda: button_click(70))

button_71 = Button(root, text=" ", padx=10, command=lambda: button_click(71))
button_72 = Button(root, text=" ", padx=10, command=lambda: button_click(72))
button_73 = Button(root, text=" ", padx=10, command=lambda: button_click(73))
button_74 = Button(root, text=" ", padx=10, command=lambda: button_click(74))
button_75 = Button(root, text=" ", padx=10, command=lambda: button_click(75))
button_76 = Button(root, text=" ", padx=10, command=lambda: button_click(76))
button_77 = Button(root, text=" ", padx=10, command=lambda: button_click(77))
button_78 = Button(root, text=" ", padx=10, command=lambda: button_click(78))
button_79 = Button(root, text=" ", padx=10, command=lambda: button_click(79))
button_80 = Button(root, text=" ", padx=10, command=lambda: button_click(80))

button_81 = Button(root, text=" ", padx=10, command=lambda: button_click(81))
button_82 = Button(root, text=" ", padx=10, command=lambda: button_click(82))
button_83 = Button(root, text=" ", padx=10, command=lambda: button_click(83))
button_84 = Button(root, text=" ", padx=10, command=lambda: button_click(84))
button_85 = Button(root, text=" ", padx=10, command=lambda: button_click(85))
button_86 = Button(root, text=" ", padx=10, command=lambda: button_click(86))
button_87 = Button(root, text=" ", padx=10, command=lambda: button_click(87))
button_88 = Button(root, text=" ", padx=10, command=lambda: button_click(88))
button_89 = Button(root, text=" ", padx=10, command=lambda: button_click(89))
button_90 = Button(root, text=" ", padx=10, command=lambda: button_click(90))

button_91 = Button(root, text=" ", padx=10, command=lambda: button_click(91))
button_92 = Button(root, text=" ", padx=10, command=lambda: button_click(92))
button_93 = Button(root, text=" ", padx=10, command=lambda: button_click(93))
button_94 = Button(root, text=" ", padx=10, command=lambda: button_click(94))
button_95 = Button(root, text=" ", padx=10, command=lambda: button_click(95))
button_96 = Button(root, text=" ", padx=10, command=lambda: button_click(96))
button_97 = Button(root, text=" ", padx=10, command=lambda: button_click(97))
button_98 = Button(root, text=" ", padx=10, command=lambda: button_click(98))
button_99 = Button(root, text=" ", padx=10, command=lambda: button_click(99))
button_100 = Button(root, text=" ", padx=10, command=lambda: button_click(100))


#Display Buttons
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=0, column=3)
button_5.grid(row=0, column=4)
button_6.grid(row=0, column=5)
button_7.grid(row=0, column=6)
button_8.grid(row=0, column=7)
button_9.grid(row=0, column=8)
button_10.grid(row=0, column=9)

button_11.grid(row=1, column=0)
button_12.grid(row=1, column=1)
button_13.grid(row=1, column=2)
button_14.grid(row=1, column=3)
button_15.grid(row=1, column=4)
button_16.grid(row=1, column=5)
button_17.grid(row=1, column=6)
button_18.grid(row=1, column=7)
button_19.grid(row=1, column=8)
button_20.grid(row=1, column=9)

button_21.grid(row=2, column=0)
button_22.grid(row=2, column=1)
button_23.grid(row=2, column=2)
button_24.grid(row=2, column=3)
button_25.grid(row=2, column=4)
button_26.grid(row=2, column=5)
button_27.grid(row=2, column=6)
button_28.grid(row=2, column=7)
button_29.grid(row=2, column=8)
button_30.grid(row=2, column=9)

button_31.grid(row=3, column=0)
button_32.grid(row=3, column=1)
button_33.grid(row=3, column=2)
button_34.grid(row=3, column=3)
button_35.grid(row=3, column=4)
button_36.grid(row=3, column=5)
button_37.grid(row=3, column=6)
button_38.grid(row=3, column=7)
button_39.grid(row=3, column=8)
button_40.grid(row=3, column=9)

button_41.grid(row=4, column=0)
button_42.grid(row=4, column=1)
button_43.grid(row=4, column=2)
button_44.grid(row=4, column=3)
button_45.grid(row=4, column=4)
button_46.grid(row=4, column=5)
button_47.grid(row=4, column=6)
button_48.grid(row=4, column=7)
button_49.grid(row=4, column=8)
button_50.grid(row=4, column=9)

button_51.grid(row=5, column=0)
button_52.grid(row=5, column=1)
button_53.grid(row=5, column=2)
button_54.grid(row=5, column=3)
button_55.grid(row=5, column=4)
button_56.grid(row=5, column=5)
button_57.grid(row=5, column=6)
button_58.grid(row=5, column=7)
button_59.grid(row=5, column=8)
button_60.grid(row=5, column=9)

button_61.grid(row=6, column=0)
button_62.grid(row=6, column=1)
button_63.grid(row=6, column=2)
button_64.grid(row=6, column=3)
button_65.grid(row=6, column=4)
button_66.grid(row=6, column=5)
button_67.grid(row=6, column=6)
button_68.grid(row=6, column=7)
button_69.grid(row=6, column=8)
button_70.grid(row=6, column=9)

button_71.grid(row=7, column=0)
button_72.grid(row=7, column=1)
button_73.grid(row=7, column=2)
button_74.grid(row=7, column=3)
button_75.grid(row=7, column=4)
button_76.grid(row=7, column=5)
button_77.grid(row=7, column=6)
button_78.grid(row=7, column=7)
button_79.grid(row=7, column=8)
button_80.grid(row=7, column=9)

button_81.grid(row=8, column=0)
button_82.grid(row=8, column=1)
button_83.grid(row=8, column=2)
button_84.grid(row=8, column=3)
button_85.grid(row=8, column=4)
button_86.grid(row=8, column=5)
button_87.grid(row=8, column=6)
button_88.grid(row=8, column=7)
button_89.grid(row=8, column=8)
button_90.grid(row=8, column=9)

button_91.grid(row=9, column=0)
button_92.grid(row=9, column=1)
button_93.grid(row=9, column=2)
button_94.grid(row=9, column=3)
button_95.grid(row=9, column=4)
button_96.grid(row=9, column=5)
button_97.grid(row=9, column=6)
button_98.grid(row=9, column=7)
button_99.grid(row=9, column=8)
button_100.grid(row=9, column=9)





#Replay Window



root.mainloop()