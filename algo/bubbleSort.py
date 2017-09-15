# Bubble Sort Implementation
def bubbleSort(myList):
	moreSwaps = True
	numSwaps = 0
	while moreSwaps:
		moreSwaps = False
		for element in range (len(myList)-1):
			if myList[element] > myList[element+1]:
				moreSwaps = True
				temp = myList[element]
				myList[element] = myList[element+1]
				myList[element+1] = temp
				numSwaps += 1
	return myList, numSwaps

if __name__=="__main__":
	unsortList = [12,5,7,18,11,6,12,4,17,1]
	[sortList, ops] = bubbleSort(unsortList)
	print("%d swaps ops were performed for this list." % ops)
	print(sortList)
