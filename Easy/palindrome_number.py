# Problem: Palindrome Number
# LeetCode Link: https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return True if x is a palindrome, and False otherwise.
# A palindrome number reads the same backward as forward.

# Intuition
# Convert the number to a string so we can easily check if it reads the same forward and backward.

# Approach
# 1. Convert the integer to a string.
# 2. Reverse the string using slicing [::-1].
# 3. Compare the original string with the reversed string.
# 4. Return True if they are equal, else False.

# Complexity
# Time complexity: O(n), where n is the number of digits in x.
# Space complexity: O(n), due to the string conversion of the number.

# Code
class Solution(object):
    def isPalindrome(self, x):
        """
        Checks if an integer is a palindrome.
        """
        s = str(x)          # Convert number to string
        return s == s[::-1] # Compare with reversed string

# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(121))   # True
    print(obj.isPalindrome(-121))  # False
    print(obj.isPalindrome(10))    # False
    print(obj.isPalindrome(12321)) # True
