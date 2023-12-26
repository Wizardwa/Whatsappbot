import google.generativeai as genai
import os

# Setting the API key
#os.environ["google_ai_studio"] = ""
def response(paste):
	prompt = paste
	# Configuring genai with the API key
	genai.configure(api_key=os.environ["google_ai_studio"])

	# Creating a GenerativeModel instance
	model = genai.GenerativeModel('gemini-pro')

	# Generating content based on the prompt
	response = model.generate_content(contents=[prompt])  # 'contents' instead of 'content'

	# Printing the generated content
	#print(response.text)
	return response.text
