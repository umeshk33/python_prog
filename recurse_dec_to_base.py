def to_str(num, base):
	conv_str = "0123456789"
	if num < base : 
		return conv_str[num]
	else : 
		return to_str(num/base, base) + conv_str[num % base]

print to_str(25, 2)
print to_str(32, 2)
