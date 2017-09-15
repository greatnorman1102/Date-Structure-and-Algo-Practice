# Intertion Sort
def insertSort(myList):
	count = 0
	for element in range (len(myList)-1):
		currentValue = myList[element+1]
		Pointer = element
		while (myList[Pointer]>currentValue) and (Pointer>=0):
			myList[Pointer+1] = myList[Pointer]
			Pointer -= 1
		myList[Pointer+1] = currentValue
		count += 1
	return myList, count

if __name__=="__main__":
	unsortList = [12,5,7,18,11,6,13,4,17,1,12]
	[sortList, ops] = insertSort(unsortList)
	print("%d swap ops were performed for this list." % ops)
	print(sortList)
