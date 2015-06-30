def bin_search(lst, item):
	print lst	
	print lst[len(lst)/2], item	
	if len(lst) == 0 :
		return False
	elif  lst[len(lst)/2] == item :
		return True

	else : 
		if lst[len(lst)/2] > item :
			return bin_search(lst[:len(lst)/2], item)

		else :
			return bin_search(lst[len(lst)/2 + 1:], item)




ref_lst = list(range(25))

print bin_search(ref_lst, 3)

