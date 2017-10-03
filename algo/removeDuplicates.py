"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 
"""

class Solution(object):
	def removeDuplicates(self, nums):
		# Check if the list is empty
		if not nums:
			return 0
		
		length = 0
		for i in range (1, len(nums)-1):
			if nums[i] != nums[length]:
				length += 1
				num[length] = nums[i]

		return length+1
