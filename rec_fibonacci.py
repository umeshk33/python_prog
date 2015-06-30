def fib(n):
	if n == 0 : 
		return 1
	elif n == 1 : 
		return 1

	else : 
		return fib(n-1) + fib(n-2)

lst = list(range(10))

for i in lst : 
	print fib(i)
