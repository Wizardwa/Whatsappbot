#!/bin/python3

import os
import sys
import pyautogui as g
import time

#Position firefox x=25 y=53
firefox = g.moveTo(x=25, y=53)

click = g.click()

#new tab
tab = g.hotkey('ctrl', 't')

search = g.typewrite("https://web.whatsapp.com/")
enter = g.hotkey('enter')
time.sleep(10)
screenshot = g.screenshot('whatsapphome.png')
#Check for new messages
new_message = g.moveTo(x=411 , y=253 )
time.sleep(2)
#green_dot = pyautogui.locateOnScreen('green.png')
click = g.click()

#copy text
message_box = g.moveTo(x=524, y=672)
double_click = g.click(clicks=2)
copy = g.hotkey('ctrl', 'c')
time.sleep(2)
#word = g.hotkey('ctrl', 'v')

#Reply
reply = g.moveTo(x=560, y=674)
click = g.click()
drop_down = g.moveTo(x=612, y=449)
click = g.click()
textbox = g.moveTo(x=562, y=729)
click = g.click()
message = g.typewrite("Whats good blud", interval=0.1)
send = g.hotkey('enter')
