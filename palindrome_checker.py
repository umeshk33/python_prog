class Deque:
	def __init__(self):
		self.items = []

	def add_rear(self, item):
		self.items.append(item)
	
	def add_front(self, item):
		self.items.insert(0, item)

	def remove_rear(self):
		self.items.pop()

	def remove_front(self):
		self.items.pop(0)

	def is_empty(self):
		if self.items.len() == 0 :
			return True
		else : 
			return False
	
	def size(self):
		return len(self.items)


def pal_checker(str1):
	deq = Deque()
	is_pal = True
	for char in str1:
		deq.add_rear(char)

	while deq.size() > 1 :
		if deq.remove_rear() != deq.remove_front() :
			is_pal = False

	return is_pal

print pal_checker('mooooooooooooooooooom')
print pal_checker('malayalam')
