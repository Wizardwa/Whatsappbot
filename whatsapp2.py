#!/bin/python3 
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from gemini import response
from generate import *
from webscrap import dalle3
import time
import pyautogui as g
import pyperclip
import re
import subprocess

user_data = os.environ["chrome_user_data"]
opt = webdriver.ChromeOptions()
opt.add_argument(f'--user-data-dir={user_data}')
#opt.add_argument("--headless")
driver = webdriver.Chrome(options=opt)
driver.get("https://web.whatsapp.com")
time.sleep(20)
#Chat xpaths /html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]
while True:
	try:
		#Check groups
		def group_chat():
			try:
				group_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span").text
				message = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[1]/span/span[2]").text
				time_sent = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]/span").text

				#check if tagged
				if "@Botbot" in message:
					#open chat
					#Crap_test = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]").click()
					Bsc_IT = driver.find_element(By.XPATH, "/html/body/div[1]/div//divdiv[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]").click()
					#Remove tag and add space
					message = re.sub('@Botbot', '', message)
					#print("This is the new message",message)
					return message
				rows = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/div[1]/div/div")
				no_rows = int(rows.get_attribute("aria-rowcount"))

				#list items
				count = 1
				k = 0
				while count <= no_rows:
					try:
						unread = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[2]/span[1]/div")
						#group with mention
						group_unread = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[2]/span[1]/div[2]")
						if unread.is_displayed():
							no_unread = unread.text
							#print("No. of unread: ", no_unread)
							#no_group_unread = group_unread.text
							#print("No of unread with mentions: ", no_group_unread)
							group_name = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[1]/div[1]/span").text
							#print("Group name: ", group_name)
							message = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[1]/span/span[2]").text
							#print("Message: ", message)
							time_sent = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[1]/div[2]/span").text
							#print("Time sent: ", time_sent)
							#check if tagged
							if "@gemini" in message:
								#open chat
								group_chat = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]").click()
								#Remove tag and add space
								message = re.sub('@gemini', '', message)
								#print("This is the new message",message)

								yield message

							k += 1
					except NoSuchElementException:
						pass
					count += 1
			except NoSuchElementException:
				pass


		#group_chat()
		#crap = group_chat()
		#print(crap)

		def read():
			#check if double check exists
			try:
				double_check = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[1]/span/div/span")
				if double_check.is_displayed():
					print("Message has been read")
			except NoSuchElementException:
				print("Message not read")
		#check all of unread messages
		def all_unread():
			#no of rows
			rows = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/div[1]/div/div")
			no_rows = int(rows.get_attribute("aria-rowcount"))
			#list items
			count = 1
			k = 0
			while count <= no_rows:
				#list_items = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]")
				#print(list_items.text)
				try:
					unread = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[2]/span[1]/div")
					if unread.is_displayed():
						username = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[1]/div[1]/div/span").text
						time_sent = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[1]/div[2]/span").text
						message = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[1]/span/span").text

						#store text to clipboard
						#message = pyperclip.copy(message)
						no_unread = unread.text

						yield no_unread,username,message,time_sent,count
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

		
		def locate_image():
			image_name = subprocess.check_output(['./local_images.sh'], stderr=subprocess.STDOUT, text=True)
			image_name = image_name.strip()
			image_path = "images" + '/' + image_name
			subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', image_path])
			#open chat
			open_chat = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]").click()
			#open_chat = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]").click()

			#send image
			reply = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
			reply.send_keys(Keys.CONTROL + "v")
			reply.send_keys(Keys.ENTER)
			send = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div").click()

		#message
		def messages():
			for k in all_unread():
				message = k[2]
				username = k[1]
				count = k[4]
				#message = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[2]/div[1]/span/span").text
				matched = ['image','photo','picture','draw','pic', 'stop']
				try:
					if "generate" in message:
						if "real" in message:
							paste = message
							#dalle3(paste)
							dalle3(paste)
						else:
							paste = message
							#image_generation(paste)
							image_generation(paste)
						#send image
						locate_image(count)
						locate_image()
						message = ""
				except TypeError:
					pass
				yield message,username,count
		#messages()
		def group_messages():
			for mess in group_chat():
				group_mess = mess

				matched = ['image','photo','picture','draw','pic', 'stop']
				try:
					if "generate" in group_mess:
						if "real" in group_mess:
							paste = group_mess
							dalle3(paste)
						else:
							paste = group_mess
							image_generation(paste)
						#send image
						locate_image()
						group_mess = ""
				except TypeError:
					pass
				yield group_mess

		#open chat
		#chat = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]").click()
		def chat():
			for chat in messages():
				count = chat[2]
				username = chat[1]
				mess = chat[0]
				open_chat = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/div[1]/div/div/div[{count}]/div/div/div/div[2]").click()
				yield mess
		#chat()
		#def reply_box(i):
			
		def send_mess(message):
			#gemini
			print(message)
			paste = message
			if paste != "":
				respond = response(paste)
				reply = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
				reply.click()
				reply.send_keys(Keys.CONTROL + "a")
				reply.send_keys(Keys.DELETE)
				reply.send_keys(respond)
				#for i in respond:
				#	reply.send_keys(i)
				#send message
				send = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()
				#time.sleep(5)
			else:
				print("Cannot reply this message")
		def reply():
			#reply message
			try:
				#check for group messages
				message = group_chat()
				send_mess(message)
				for mess in group_messages():
					message = mess
					send_mess(message)
				#single chats
				for chats in chat():
					message = chats
					send_mess(message)

						
			except (TypeError, NoSuchElementException):
				pass
		reply()
	except (ValueError,StaleElementReferenceException):
		print("You have a ValueError")
driver.quit()