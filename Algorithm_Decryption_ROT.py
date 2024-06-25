#Link -> https://en.wikipedia.org/wiki/ROT13
#Link to code -> https://www.geeksforgeeks.org/rot13-cipher/
# Dictionary to lookup the index of alphabets
dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
		'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
		'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
		'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
		'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

# Dictionary to lookup alphabets
# corresponding to the index after shift
dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
		6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
		11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
		16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
		21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'}


def decrypt_rot01(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 1 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot02(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 2 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot03(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 3 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot04(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 4 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot05(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 5 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot06(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 6 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot07(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 7 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot08(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 8 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot09(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 9 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot10(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 10 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot11(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 11 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot12(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 12 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot13(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 13 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot14(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 14 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot15(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 15 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot16(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 16 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot17(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 17 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot18(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 18 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot19(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 19 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot20(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 20 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot21(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 21 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot22(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 22 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot23(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 23 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot24(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 24 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher

def decrypt_rot25(message):
	decipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			# looks up the dictionary and
			# subtracts the shift to the index
			num = ( dict1[letter] - 25 + 26) % 26
			# looks up the second dictionary for the
			# shifted alphabets and adds them
			decipher += dict2[num]
		else:
			# adds space
			decipher += ' '

	return decipher