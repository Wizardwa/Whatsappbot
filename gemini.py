import google.generativeai as genai
import os
import pyautogui as g

def response(paste):
    prompt = paste

    # Configuring genai with the API key
    genai.configure(api_key=os.environ["google_ai_studio"])

    # Creating a GenerativeModel instance
    model = genai.GenerativeModel('gemini-pro')
                
    # Generating content based on the prompt
    response = model.generate_content(prompt)
    #multi-turn conversation
        
    #chat = model.start_chat(history=[])
    #response = chat.send_message(prompt)

    
    return response.text
