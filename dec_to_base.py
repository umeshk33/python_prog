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



def dec_to_base(num, base):
	if num == 0 or base == 0 :
		return 0
	rem = num
	s = stack()
	lst = []
	while rem > 0 :
		s.push(rem%base)
		rem = int (rem / base)

	while not s.is_empty()	:
		lst.append(s.pop())

	return lst

print dec_to_base(25, 2)

