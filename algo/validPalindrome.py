"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
	def isPalindrome(self, s):
		front = 0
		back = len(s)-1
		while front < back:
			# string.isalnum() returns True if the string are alphanumeric
			# (either alphabets or numbers). If not, it returns False
			while front < back and not s[front].isalnum():
				front += 1
			while front < back and not s[back].isalnum():
				back -= 1
			if s[front].lower() != s[back].lower():
				return False
			front += 1
			back -= 1
		return True
