#!/bin/python3

import time
import pyautogui as p
import pyscreenshot as screen

time.sleep(5)

cursor = p.moveTo(x=142,y=146)
image = screen.grab(bbox=(142,142,255,175))
image.save("sample.png")

#dark_theme = "dark.png"

sample = open("sample.png","rb").read()
dark_theme = open("dark.png","rb").read()

if sample == dark_theme:
	print("dark theme on")
else:
	print("white theme on")
