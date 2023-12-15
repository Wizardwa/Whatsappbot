#!/bin/python3 

#reply messages

def replies(paste):
	if paste == "hello":
		message = "Hello too"
	elif paste == "hey":
		message = "Whats good"
	elif paste == "itakuwa aje":
		message = "Hamna story"
	elif paste == "mambo":
        	message = "poa"
	elif paste == "how are you" or paste == "how is you":
		message = "Am fine, how about you"
	elif paste == "how is the going":
		message = "Great"
	elif paste == "uko area":
		message = "yeah"
	elif paste == "uko kejani":
		message = "yeah"
	elif paste == "unado":
		message = "kuchill"
	elif paste == "niambie":
		message = "sina maneno"
	elif paste == "we mzee" or "wee mzee":
		message = "Unasemaje"
	else:
		message = "Hi"
	return message
