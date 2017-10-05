"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
	def isValid(self, s):
		stack = []
		dictionary = {"]":"[", ")":"(", "}":"{"}

		for char in s:
			if char in dictionary.values():
				stack.append(char)
			elif char in dictionary.keys():
				if stack == [] or dictionary[char] != stack.pop():
					return False
			else:
					return True
		return stack == []
