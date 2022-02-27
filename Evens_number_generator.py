def even_numbers_generator(start, end):
	num = start
	
	while num <= end:
		
		yield num
		num +=1

for num in even_numbers_generator(1,10):
    if num %2 == 0:
	    print(num)
