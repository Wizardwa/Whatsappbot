#!/bin/python3

import subprocess
import pyautogui as g
import time
import os

def photo():
	try: 
		photo = g.locateOnScreen("photo.png", confidence=0.9)
		g.moveTo(x=photo[0], y=photo[1])
		g.click()
		locate = g.moveTo(x=600, y=600)
		g.click()
		g.moveTo(x=1254, y=136)
		g.click()
		g.moveTo(x=1335,y=137)
		g.click()
		#reply = g.moveTo(x=560, y=674)
		#click = g.click()
		#drop_down = g.moveTo(x=612, y=449)
		#click = g.click()
		textbox = g.moveTo(x=562, y=729)
		click = g.click()

		#image_name = os.system('./image.sh')
		result = subprocess.check_output(['./image.sh'], stderr=subprocess.STDOUT, text=True)
		return result.strip()
		#print("position: ", photo[0], photo[1])
		#print('\n',image_name)

	except g.ImageNotFoundException:
		#print("No image was sent")
		pass
