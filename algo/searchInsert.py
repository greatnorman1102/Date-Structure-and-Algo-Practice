"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 52
[1,3,5,6], 21
[1,3,5,6], 74
[1,3,5,6], 00 
"""

class Solution(object):
	def searchInsert(self, nums, target):
		# Check if the target could fit at either beginning or end of the list
		if target < nums[0]:
			return 0
		if target > nums[-1]:
			return len(nums)

		# Setup double pointer for the search
		front = 0
		back = len(nums) - 1
		while front <= back:
			
			pivot = (front + back) / 2
			# If target is less than pivot, move the tail pointer to the left of pivot
			if nums[pivot] > target:
				back = pivot - 1
				if back >= 0:
					if nums[back] < target:
						return back+1
				else:
					return 0
			# If target is more than pivot, move the head pointer to the right of pivot
			elif nums[pivot] < target:
				front = pivot + 1
				if front < len(nums):
					if nums[front] > target:
						return front
				else:
					return len(nums)
			# If target is equal to the pivot, return pivot index
			else:
				return pivot
