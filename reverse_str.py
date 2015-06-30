def rev_str(str):
	new_str = ""
	for i in range(len(str)):
		new_str += str[len(str) - i - 1]
	return new_str

print rev_str('hello')
