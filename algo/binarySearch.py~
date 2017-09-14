# Binary Search

def binarySearch(myItem, myList):
	found = False
	bottom = 0
	top = len(myList)+1

	while bottom<=top and not found:
		middle = (bottom+top)//2
		if myList[middle]==myItem:
			found = True
		elif myList[middle] < myItem:
			bottom = middle + 1
		elif myList[middle] > myItem:
			top = middle - 1
	return found, middle
			
if __name__=="__main__":
	numberList = [1,4,6,7,9,10,14,17,18,20,26,47,58,62,90,100]
	item = int(input("What number are you looking for?"))
	if item < numberList[0]:
		numberList.insert(0,item)
		print("Your number is not found but is been added to the list.", numberList)
	elif item > numberList[-1]:
		numberList.append(item)
		print("Your number is not found but is been added to the list.", numberList)
	else:
		[isitFound,index] = binarySearch(item, numberList)
		if isitFound:
			print("You number is found at the %d position." % (index+1))
		else:
			# Add number to the list
			numberList.insert(index+1, item)
			print("Your number is not found but is been added to the list.", numberList)
