#!/bin/python3 

#Generate temporary mail

import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time


opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

driver = webdriver.Chrome()
driver.get("https://10minutemail.net/")
time.sleep(10)

driver.quit()

