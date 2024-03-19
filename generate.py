#!/bin/python3 

import os
import re
import requests
import json
import time
import PIL.Image as image
import random
import string
import pyautogui as g

def image_generation(paste):
    prompt = paste
    def order(prompt):
        try:
            #prompt = paste
            url = "https://api.neural.love/v1/ai-art/generate"
            api = os.environ["neural_love"]
            payload = {
                "style": "FANTASY",
                "prompt": prompt,
                "layout": "SQUARE",
                "amount": 1,
                "isPublic": True,
                "isPriority": False,
                "isHd": False,
                "model": "default",
                "steps": 30,
                "cfgScale": 7.5,
                "autoClean": False
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": "Bearer " + api
                }

            response = requests.post(url, json=payload, headers=headers)
            order = response.text
            data = eval(order)
            order_id = data["orderId"]
        except NameError:
            textbox = g.moveTo(x=562, y=729)
            click = g.click()
            g.typewrite("Banned words used, rephrase", interval=0.1)
            g.hotkey('enter')

        return order_id

    order = order(prompt)

    def check_order_info(order):
        time.sleep(120)
        api = os.environ["neural_love"]
        url = f"https://api.neural.love/v1/ai-art/orders/{order}"
        headers = {
            "accept": "application/json",
            "authorization": "Bearer "+ api
        }

        response = requests.get(url, headers=headers)

        order_info = response.text
        order_info_json = json.loads(order_info)

        if 'output' in order_info_json and len(order_info_json['output']) > 0:
            full_webp = order_info_json['output'][0].get('fullWebp')
            if full_webp:
                full_webp = full_webp
            else:
                print("No 'fullWebp' found in the 'output' data.")
        else:
            print("No 'output' data found in the JSON.")


        return full_webp

    #continuously call check_order_info and add wait time

    image_url = check_order_info(order)
    check = "No 'output' data found in the JSON."

    if image_url == check:
        while image_url == check:
           image_url = check_order_info(order)
    else:
        pass

    def generate_random_word(length=5):
        letters = string.ascii_lowercase  # Pool of lowercase letters
        return ''.join(random.choice(letters) for _ in range(length))

    random_word = generate_random_word()

    download_image = os.system(f'wget \"{image_url}\" -O images/{random_word}.webp')

    time.sleep(5)
    #convert from .webp to .png
    img = image.open(f"images/{random_word}.webp").convert("RGB")
    img.save(f"images/{random_word}.png", "png")




















