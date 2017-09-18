# Quick sort algorithm Ops = nlog(n)

def quickSort(myList, start, end):
	if start < end:
		# partition on the list
		pivot = partition(myList, start, end)
		# sort both halves
		quickSort(myList, start, pivot-1)
		quickSort(myList, pivot+1, end)
	return myList

def partition(myList, start, end):
	pivot = myList[start]
	print(pivot)
	left = start+1
	right = end
	done = False
	while not done:
		while left <= right and myList[left] <= pivot:
			left += 1
		while left <= right and myList[right] >= pivot:
			right -= 1
		if right < left:
			done = True
		else:
			# swap element places
			temp = myList[left]
			myList[left] = myList[right]
			myList[right] = temp
			print(myList)
	# swap start with myList[right]
	temp = myList[start]
	myList[start] = myList[right]
	myList[right] = temp
	return right


if __name__=="__main__":
	numberList = [100,98,89,86,77,75,72,61,60,58,4,17,27,6,18,20,1]
	sortList = quickSort(numberList, 0, (len(numberList)-1))
	print("The sorted list is follow:")
	print(sortList)
