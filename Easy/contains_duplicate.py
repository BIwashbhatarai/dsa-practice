# 217. Contains Duplicate
# Easy | LeetCode Problem

"""
Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct.

Examples:
---------
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# --------------------------------------------------
# Solution 1: Using Set (Efficient O(n) time, O(n) space)
# --------------------------------------------------
class SolutionSet(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

# Example
obj1 = SolutionSet()
print("Set Solution:", obj1.containsDuplicate([1, 2, 3, 4, 5]))   # False
print("Set Solution:", obj1.containsDuplicate([1, 2, 3, 1]))     # True


# --------------------------------------------------
# Solution 2: Using List (Brute Force O(n^2) worst-case, O(n) space)
# --------------------------------------------------
class SolutionList(object):
    def containsDuplicate(self, nums):
        seen = []
        duplicate = []
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate.append(nums[i])
            else:
                seen.append(nums[i])
        return True if duplicate else False

# Example
obj2 = SolutionList()
print("List Solution:", obj2.containsDuplicate([1, 2, 3, 4, 5]))  # False
print("List Solution:", obj2.containsDuplicate([1, 2, 3, 1]))    # True
