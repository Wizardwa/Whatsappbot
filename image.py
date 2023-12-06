#!/bin/python3

from screen_search import *
import pyautogui

search = Search("firedox.png")

pos = search.imagesearch()

if pos[0] != -1:
	print("position : ", pos[0], pos[1])
	pyautogui.moveTo(pos[0], pos[1])
	click = pyautogui.click()
else:
	print("Image not found")
