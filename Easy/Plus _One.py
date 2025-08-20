# Problem: Plus One
# LeetCode Link: https://leetcode.com/problems/plus-one/
#
# Given a large integer represented as an array of digits, increment the integer by one
# and return the resulting array of digits.

# Intuition
# Treat the list of digits as a single number, increment it by 1, then split it back into digits.

# Approach
# 1. Convert the list of digits to a single integer.
# 2. Add 1 to the integer.
# 3. Convert the result back to a list of digits.

# Complexity
# Time complexity: O(n), where n is the number of digits.
# Space complexity: O(n), for storing the resulting list of digits.

# Code
class Solution(object):
    def plusOne(self, digits):
        """
        Increment a list-represented integer by one.
        """
        num = int("".join(map(str, digits)))
        num += 1
        
        return list(map(int, str(num)))
    
obj = Solution()
print(obj.plusOne([1,2,3,4]))