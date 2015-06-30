def rev_list(lst):
	if len(lst) == 0 :
		return []
	
	x, y = lst[0], lst[1:]

	return rev_list(y) + [x]

a = list(range(10))
print rev_list(a)
