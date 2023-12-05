#!/bin/python3 

import pyautogui
import os
import sys
import time

#position of Software Updater x=20, y=318

position = pyautogui.moveTo(x=20, y=318)

#show current position
current_post = pyautogui.position()
print(current_post)

#click event

click = pyautogui.click()

#move to the next position x=960 y=487
time.sleep(18)

#position_ok = pyautogui.moveTo(x=960, y=487)
locate_ok = pyautogui.locateOnScreen('ok.png')
click = pyautogui.click()

#write something on the screen

keyboard = pyautogui.typewrite("Code is working\n")
time.sleep(2)

try:
    keyboard = pyautogui.hotkey('ctrl', 'c')
    print('\n')
   #os.system('clear')
except KeyboardInterrupt:
    os.system('clear')

