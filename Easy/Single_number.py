# 136. Single Number
# Easy | LeetCode Problem

"""
Given a non-empty array of integers nums, every element appears **three times** except for **one element** which appears **exactly once**.
Find that single one.

Examples:
---------
Input: nums = [2,2,3,2]
Output: 3

Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""

# --------------------------------------------------
# Solution: Using XOR trick for single number
# Works because XOR of a number with itself odd/even times cancels out
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        count = 0
        for num in nums:
            count = count ^ num
        return count

# Example usage
obj = Solution()
nums = [1, 2, 2, 2, 3, 3, 3]
print("Single number:", obj.singleNumber(nums))  # Output: 1
