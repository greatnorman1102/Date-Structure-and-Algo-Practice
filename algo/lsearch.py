# Linear search

def linearSearch(myItem, myList):
	found = False
	position = 0
	
	while position < len(myList) and not found:
		if myList[position] == myItem:
			found = True
		position = position +1
	return found, position

if __name__=="__main__":
	shopping = ["apples", "bananas","chocolate","watermelon"]
	item = input("What item do you want to find?")
	[isitFound, index] = linearSearch(item, shopping)
	if isitFound:
		print("Your item is in the list, it's the number %d item on the list." % index)
	else:
		shopping.append(item)
		print (shopping)
		print("Your item is not in the list, but it is now been added.")
	