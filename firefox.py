#!/bin/python3

import os
import sys
import pyautogui as g
import time
from screen_search import *
import tkinter as tk  
from replies import replies
from game import choices
from gemini import response
import pyscreenshot as screen

#Position firefox x=25 y=53
#firefox = g.moveTo(x=25, y=53)

"""search = Search("firedox.png")

pos = search.imagesearch()

if pos[0] != -1:
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    click = pyautogui.click()
else:
    print("Image not found")"""
locate = g.locateCenterOnScreen("firedox.png", confidence=0.5) 
pos = locate
g.moveTo(pos[0], pos[1])
click = g.click()

#new tab
tab = g.hotkey('ctrl', 't')

search = g.typewrite("https://web.whatsapp.com/", interval=0.1)
enter = g.hotkey('enter')
time.sleep(15)
def screenshot():
    screenshot = g.screenshot('whatsapphome.png')
    cursor = g.moveTo(x=142,y=146)
    image = screen.grab(bbox=(142,142,255,175))
    image.save("sample.png")

screenshot()
#Check for new messages
while True:
    try:
        #new_message = g.moveTo(x=411 , y=253 )


            
        def themes():
            sample = open("sample.png","rb").read()
            dark_theme = open("dark.png","rb").read()
            white_theme = open("white.png","rb").read()

            if sample == dark_theme:
                theme = "new.png"
            if sample == white_theme:
                theme = "white-theme-dot.png"

            return theme

        #theme = themes(sample)
        def unread():
            theme = themes()
            unread = g.locateOnScreen(theme, confidence=0.9)
            #copy = g.hotkey('ctrl', 'c')
            g.moveTo(unread[0]-20, unread[1])
            click = g.click()
            time.sleep(2)
            locate = g.moveTo(x=372, y=244)
            locate_text = g.moveTo(x=518, y=672)
            time.sleep(1)
            #locate_text = g.moveTo(x=524, y=672)
            double_click = g.click(clicks=3)
            copy = g.hotkey('ctrl', 'c')

            #Tk
            root = tk.Tk()
            root.withdraw()

            paste = root.clipboard_get()
            paste = paste.lower()

            time.sleep(2)

            #print text
            print("Message says: \n") 
            print(paste)

            return paste

        unread = unread()
        paste = unread

        #Reply
        #call func if numeric or word 
        if(paste == "game"):
            mess = choices(paste)
        elif(paste == "stop"):
            break
        else:
            mess = response(paste)
        def textbox():
            reply = g.moveTo(x=560, y=674)
            click = g.click()
            drop_down = g.moveTo(x=612, y=449)
            click = g.click()
            textbox = g.moveTo(x=562, y=729)
            click = g.click()
            
        textbox()
        reply = g.typewrite(mess, interval=0.1)
        send = g.hotkey('enter')
    except g.ImageNotFoundException:
        pass
