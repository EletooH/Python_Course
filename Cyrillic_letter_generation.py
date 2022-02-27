def cyrillic():
	start = 1040
	end = 1070
	letter = start
	
	while letter <= end+1:
		
		yield chr(letter)
		letter +=1

for letter in cyrillic():
	print(letter)
