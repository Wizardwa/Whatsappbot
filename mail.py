#!/bin/python3 

import requests

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/one_mail/id/%7Bmail_id%7D/"

headers = {
	"X-RapidAPI-Key": "aebf7a7aa7mshb50d3412fbd4effp1bf3d0jsnf2c7cc167c68",
	"X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
