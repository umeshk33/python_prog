def factorial(num):
	if num < 1 : 
		return "Please input a number is less than 1"
	if num == 1 : 
		return 1
	else : 
		return num * factorial(num - 1)
	
print factorial(4)
