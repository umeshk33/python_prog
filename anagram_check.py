def anagram_check(s1, s2):
	a_list = list(s1)
	b_list = list(s2)
	a_sorted = sorted(a_list)
	b_sorted = sorted(b_list)
	if a_sorted == b_sorted:
		return "true"
	else :
		return "false"


print anagram_check("typhon", "python")
