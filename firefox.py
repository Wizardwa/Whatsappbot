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
from multi import photo
from multimodal import multi_modal
from webscrap import dalle3
import pyscreenshot as screen
import clipboard
from generate import *
import re
import subprocess

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

        def unread():
            theme = themes()
            unread = g.locateOnScreen(theme, confidence=0.9)
            #copy = g.hotkey('ctrl', 'c')
            g.moveTo(unread[0]-20, unread[1])
            #locate = g.moveTo(x=372, y=244) changed for concurrency 
            click = g.click()
            time.sleep(2)

            
            

        def text():
            locate_text = g.moveTo(x=518, y=672)
            double_click = g.click(clicks=3)
            copy = g.hotkey('ctrl', 'c')
            time.sleep(1)
            #locate_text = g.moveTo(x=524, y=672)
            #Tk
            root = tk.Tk()
            root.withdraw()

            paste = root.clipboard_get()
            paste = paste.lower()

            time.sleep(2)

            #print text
            print(f"Message says: {paste}")

            #matched = ['image','photo','picture','draw','pic']

            if "image" in paste:
                if "real" in paste:
                    dalle3(paste)
                else:
                    image_generation(paste)
                
                image_name = subprocess.check_output(['./local_images.sh'], stderr=subprocess.STDOUT, text=True)
                image_name = image_name.strip()
                image_path = "images" + '/' + image_name
                subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', image_path])
                #textbox = g.moveTo(x=562, y=729)
                #click = g.click()
                send = g.hotkey('ctrl', 'v')
                send = g.hotkey('enter')
                time.sleep(2)
                send = g.hotkey('enter')
                paste = ""



            return paste

        #check for unread messages
        unread()

        #call to generate image


        paste = text()
        photo = photo()

        if photo != None:
            mess = multi_modal(photo)
        else:
            mess = response(paste)

        def textbox():
            #reply = g.moveTo(x=560, y=674)
            #click = g.click()
            #drop_down = g.moveTo(x=612, y=449)
            #time.sleep(5)
            #click = g.click()
            textbox = g.moveTo(x=562, y=729)
            click = g.click()
            
        textbox()

        reply = g.typewrite(mess, interval=0.1)
        send = g.hotkey('enter')
    except (g.ImageNotFoundException,TypeError,ValueError,UnboundLocalError):
        pass
