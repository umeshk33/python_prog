class stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]
	
	def size(self):
		return len(self.items)




def check_par(str):
	lst = list(str)
	s = stack()
	for i in lst :
		if i == '(' :
			s.push(i)
		else :
			if(s.is_empty()) :
				return "Not Balanced"
			else :
				s.pop()
	if(s.is_empty()) :
		return "Balanced"
	else :
		return "Not Balanced"

print check_par('(()())')
