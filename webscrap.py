#!/bin/python3

#web scrapping imgcreator with selenium
import os
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open a Chrome browser
driver = webdriver.Chrome()

# Navigate to the Zmo AI Image Creator text input page
driver.get("https://imgcreator.zmo.ai/ai-generator?type=text_input")

# Wait for the text input field to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "text-input"))
)

# Find the text input field and enter your prompt
text_input_field = driver.find_element(By.ID, "text-input")
text_input_field.send_keys("A photorealistic image of a cat wearing a wizard hat, sitting on a stack of books.")

# Find the "Generate" button and click it
generate_button = driver.find_element(By.ID, "generate-button")
generate_button.click()

# Wait for the image to be generated
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "generated-image"))
)

# Find the generated image and get its URL
generated_image = driver.find_element(By.CLASS_NAME, "generated-image")
image_url = generated_image.get_attribute("src")

# Create a directory to save the image
directory = "generated_images"
os.makedirs(directory, exist_ok=True)

# Use wget to download the image
wget.download(image_url, out=os.path.join(directory, "generated_image.png"))

# Print a success message
print("Image generated and saved to file!")
