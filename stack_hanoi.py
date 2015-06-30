class stack:
	def __init__(self, name):
		self.items = []
		self.name = name
	
	def get_name(self):
		return self.name

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


lst = list(range(5))
lst = lst[::-1]
print lst
beg = stack("begin")
for i in lst:
	beg.push(i)

aux = stack("aux")
end = stack("end")

def move_tower(height, fr_pole, to_pole, aux_pole):
	if height >=1 :
		move_tower(height - 1, fr_pole, aux_pole, to_pole)
		move_disk(fr_pole, to_pole)
		move_tower(height - 1, aux_pole, to_pole, fr_pole)


def move_disk(a, b):
	print "moving",  a.peek(), "from", a.get_name(), "to", b.get_name()
	b.push(a.pop())


move_tower(5, beg, end, aux)
