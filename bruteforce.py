#!/usr/bin/env python3

from crypt import crypt
import random
import itertools
import string

word_to_bruteforce = "lovecum"

def _salt(c):
	c = ord(c)
	if 58 <= c <= 64:
		return chr(c + 7)
	elif 91 <= c <= 96:
		return chr(c + 6)
	elif 46 <= c <= 122:
		return chr(c)
	return '.'

def genTripcode(password):
	salt = (password[:8] + 'H.')[1:3]
	salt = "".join(_salt(c) for c in salt)
	trip_final = crypt(password[:8], salt)
	return trip_final[-10:]

words = map(''.join, itertools.product(string.ascii_letters + string.digits, repeat=8))
for word in words:
	tripcode = genTripcode(word)
	if (tripcode.startswith(word_to_bruteforce)):
		print("Password: " + word + " - Tripcode: " + tripcode)
		break