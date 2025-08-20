# Problem: Two Sum
# LeetCode Link: https://leetcode.com/problems/two-sum/
#
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers
# such that they add up to `target`.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        Brute force solution: checks all pairs to find the target sum.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# --- Example Usage ---
if __name__ == "__main__": 
    obj = Solution()
    
    # Test cases
    print(obj.twoSum([1,2,3,4,5], 5))      # Expected: [0, 3]
    print(obj.twoSum([5,2,7,3,1], 7))      # Expected: [1, 2]
    print(obj.twoSum([2,6,3,5,7], 9))      # Expected: [0, 2]
    print(obj.twoSum([2,3,7,4,9], 12))     # Expected: [2, 3]
