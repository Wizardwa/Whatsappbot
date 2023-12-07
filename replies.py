#!/bin/python3 

#reply messages

def replies(paste):
	if paste == "Hello":
		message = "Hello too"
	elif paste == "Hey":
		message = "Whats good"
	elif paste == "Itakuwa aje":
		message = "Hamna story"
	elif paste == "mambo":
        	message = "poa"
	else:
		message = "You have not typed anything"
	return message
