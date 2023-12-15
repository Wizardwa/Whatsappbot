#!/bin/python3

import pyscreenshot as screen
import pyautogui as p

cursor = p.moveTo(x=142, y=146)
im = screen.grab(bbox=(142,142,255,175))
im.show()

im.save('white.png')
