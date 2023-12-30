#!/bin/python3 

import pyautogui as g
import os
import time 

login = g.locateOnScreen("login.png", confidence=0.9)
g.moveTo(x=login[0], y=login[1])
#print("position: " ,login[0], login[1])
g.click()
time.sleep(10)
OR = g.locateOnScreen("or.png", confidence=0.9)
g.moveTo(x=OR[0], y=OR[1])
#print("position of OR: ", OR[0], OR[1])
#relative position from OR
email = g.moveTo(x=545, y=379)
g.click()
g.typewrite("crapguy675@gmail.com", interval=0.1)
back_OR = g.moveTo(x=OR[0], y=OR[1])
g.click()
password = g.moveTo(x=502, y=441)
g.click()
g.typewrite("crapisgood", interval=0.1)

#click to login/signup
login_button = g.moveTo(x=545, y=520)
g.click()

time.sleep(10)
#After login
text_box = g.moveTo(x=269, y=296)
g.click()
g.typewrite("a photo of a black woman", interval=0.1)
generate = g.locateCenterOnScreen("generate.png", confidence=0.9)
g.moveTo(x=generate[0], y=generate[1])
g.click()

time.sleep(120)



