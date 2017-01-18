#Fun little script for generating a profile pic by Erik Lanning on 1/18/2017
from Tkinter import *
from math import cos, sin, tan, log, sqrt
import random

def drawingFunc(x):
	return -(sin(x) + cos(x))

tk = Tk()
drawingBoard = Canvas(tk, width=400, height=400, background='black')
drawingBoard.pack()

bounds = 400
thickness = 300

color = ["green", "blue", "violet"]

for x in range(1, bounds):
	y = drawingFunc(x)
	drawingBoard.create_line(x, y, x+thickness, y+thickness, fill=random.choice(color))

for x in range(bounds, 1, -1):
	y = x
	x = drawingFunc(y)
	drawingBoard.create_line(x, y, x+thickness, y+thickness, fill=random.choice(color))
	
tk.mainloop()