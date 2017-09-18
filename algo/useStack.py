# implement functions of a stack, push, pop, size, reportonStack

def useStack():
	stack = []
	choice = -1
	while choice != 4:
		print("1. Push on to stack")
		print("2. Pop from stack")
		print("3. Print stack")
		print("4. Exit")
		choice = int(input("Enter your choice >>"))
		if choice == 1:
			nextItem = input("What do you want to add to the stack")
			stack.append(nextItem)
		if choice == 2:
			# delete the top of current stack
			if stack == []:
				print("The stack is empty, nothing to pop.")
			else:
				print("Removing %s on the stack." % stack[-1])
				del stack[-1]
		if choice == 3:
			print(stack)
		if choice == 4:
			return 0

if __name__=="__main__":
	useStack()
