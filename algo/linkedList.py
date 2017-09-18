# Implementing Linked List Class in OOP
# Linked List Class
class node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next
	def set_next(self, new_next):
		self.next = new_next

class LinkedList:
	def __init__(self, head=None):
		self.head = head
	def insert(self, data):
		new_node = node(data)
		new_node.set_next(self.head)
		self.head = new_node
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count
	def search(self, data):
		current = self.head
		found = False
		while current and not found:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current in None:
			raise ValueError("Data not in list")
		return current
	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and not found:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
	def peek(self):
		current = self.head
		while current:
			data = current.get_data()
			current = current.get_next()
			print(data)
