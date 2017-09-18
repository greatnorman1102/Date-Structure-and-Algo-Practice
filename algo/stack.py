# Implementing a stack using OOP
# The stack class

class stack:
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		del self.items[-1]
	def isEmpty(self):
		if self.items==[]:
			return True
		else:
			return False
	def size(self):
		return len(self.items)
	def peek(self):
		print(self.items)
