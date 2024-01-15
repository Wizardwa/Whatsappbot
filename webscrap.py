#!/bin/python3

#web scrapping imgcreator with selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import string
import random
import os
import PIL.Image as im

def dalle3(paste):
    prompt = paste
    driver = webdriver.Chrome()
    driver.get("https://imgcreator.zmo.ai/ai-generator?url=/ai-generator&type=text_input")

    try:
        assert driver.title == "The Ultimate AI Photo Generator | Magic Background Generate For Your Photo"
        sign = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[1]/header/div[2]/div")))
        if sign.is_displayed():
            sign.click()
            time.sleep(5)
            modal = driver.find_element(By.CLASS_NAME, 'modal-container')
            email = driver.find_element(By.ID, 'el-id-1024-44')
            email.send_keys("ritixam303@usoplay.com")
            password = driver.find_element(By.ID, 'el-id-1024-45')
            password.send_keys("crapisgood")
            login_button = driver.find_element(By.XPATH, "/html/body/div[17]/div/div[1]/div[1]/div[6]").click()
            text_box = driver.find_element(By.ID, 'el-id-1024-22')
            text_box.send_keys(prompt)
            realistic = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div/div/div[4]/div/div").click()
            create_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[2]/div/button[1]").click()
            time.sleep(5)
            try:
                premium_button = driver.find_element(By.XPATH, "/html/body/div[15]/div/div/div[2]/div[2]/p")
                if premium_button.is_displayed():
                    print("Use another email")
                    driver.quit()
                else:
                    time.sleep(180)
                    image = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[1]/img")
                    image_url = image.get_attribute("src")
                    def generate_random_word(length=5):
                        letters = string.ascii_lowercase  # Pool of lowercase letters
                        return ''.join(random.choice(letters) for _ in range(length))
                
                    random_word = generate_random_word()
                    download_image = os.system(f'wget \"{image_url}\" -O images/{random_word}.webp')

                    time.sleep(5)
                    #convert from .webp to .png
                    img = im.open(f"images/{random_word}.webp").convert("RGB")
                    img.save(f"images/{random_word}.png", "png")
            except NoSuchElementException:
                pass
                

            
        else:
            print("Element not found")

    except AssertionError:
        print("You are on a different page")




#driver.quit()
