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


def encrypt_rot01(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 1 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot02(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 2 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot03(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 3 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot04(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 4 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot05(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 5 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot06(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 6 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot07(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 7 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot08(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 8 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot09(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 9 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot10(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 10 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot11(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 11 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot12(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 12 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot13(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 7 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot14(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 14 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot15(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 15 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot16(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 16 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot17(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 17 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot18(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 18 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot19(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 19 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot20(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 20 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot21(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 21 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot22(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 22 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot23(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 23 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot24(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 24 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher

def encrypt_rot25(message):
	cipher = ''
	for letter in message:
		# checking for space
		if(letter != ' '):
			# looks up the dictionary and
			# adds the shift to the index
			num = ( dict1[letter] + 25 ) % 26
			# looks up the second dictionary for
			# the shifted alphabets and adds them
			cipher += dict2[num]
		else:
			# adds space
			cipher += ' '

	return cipher
