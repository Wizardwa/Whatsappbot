#!/bin/python3

import google.generativeai as genai
import os
import PIL.Image as image

def multi_modal(photo):
    prompt = photo
    img = image.open(prompt)
    genai.configure(api_key=os.environ["google_ai_studio"])

    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(img)

    return response.text
