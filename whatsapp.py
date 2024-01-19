#!/bin/python3 

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from gemini import response
from generate import *
from webscrap import dalle3
import time
import pyautogui as g

user_data = "/home/ewaat/snap/chromium/common/chromium/Default"
opt = webdriver.ChromeOptions()
opt.add_argument(f'--user-data-dir={user_data}')
driver = webdriver.Chrome(options=opt)
driver.get("https://web.whatsapp.com")
time.sleep(20)

#Chat xpaths /html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]
def read():
	#check if double check exists
	try:
		double_check = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[1]/span/div/span")
		if double_check.is_displayed():
			print("Message has been read")
	except NoSuchElementException:
		print("Message not read")

def locate_image():
	image_name = subprocess.check_output(['./local_images.sh'], stderr=subprocess.STDOUT, text=True)
	image_name = image_name.strip()
	image_path = "images" + '/' + image_name
	subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', image_path])

#check all of unread messages
def all_unread():
	#no of rows
	rows = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div")
	no_rows = int(rows.get_attribute("aria-rowcount"))

	#list items
	count = 1
	k = 0
	while count <= no_rows:
		list_items = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]")
		#print(list_items.text)
		try:
			unread = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[2]/span[1]/div")
			if unread.is_displayed():
				username = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[1]/div[1]/div/span").text
				time_sent = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[1]/div[2]/span").text
				message = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[1]/span/span").text
				no_unread = unread.text
				yield no_unread,username,message,time_sent
				k += 1
				#call message func
				#messages(message,username)
		except NoSuchElementException:
			pass
		count += 1
#all_unread()

def unread_preview():
	func_call = all_unread()
	for i in func_call:
		no_unread = i[0]
		username = i[1]
		message = i[2]
		time_sent = i[3]
		if no_unread == '1':
			print(f"You have {no_unread} new message from {username} at {time_sent}")
			print(f"Message says: {message}")
		elif no_unread == '':
			print(f"You have marked message from {username} as unread")
			print(f"Message says: {message}")
		else:
			print(f"You have {no_unread} new messages from {username} at {time_sent}")
			print(f"Last message says: {message}")

unread_preview()

#message
def messages():
	func_call = all_unread()
	message = message[2]
	#message = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[1]/span/span").text
	matched = ['image','photo','picture','draw','pic', 'stop']
	if "image" in message:
		if "real" in message:
			paste = message
			#dalle3(paste)
		else:
			paste = message
			#image_generation(paste)
		#send image
		#locate_image()
		message = ""
	return message

#open chat
#chat = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]").click()
def chat():
	messages()
	open_chat = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]").click()

#chat()
"""def reply():
	#reply message
	reply = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
	reply.click()
	reply.send_keys(Keys.CONTROL + "a")
	reply.send_keys(Keys.DELETE)
	#gemini
	paste = message
	response = response(paste)
	reply.send_keys(response)

	#send message
	send = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()
"""

time.sleep(10)














driver.quit()
