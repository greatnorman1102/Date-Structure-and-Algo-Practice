# Implementing a queue using OOP
# The Queue class

class queue:
	def __init__(self):
		self.items=[]
	def isEmpty(self):
		if self.items==[]:
			return True
		else:
			return False
	def add(self, item):
		self.items.append(item)
	def delete(self):
		del self.items[0]
	def size(self):
		return len(self.items)
	def peek(self):
		print(self.items)
