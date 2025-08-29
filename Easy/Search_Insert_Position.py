"""
LeetCode Problem 35: Search Insert Position (Easy)
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If the target is not found, return the index where it would be inserted in order.
The algorithm runs in O(log n) time using binary search.
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid          # Target found
            elif nums[mid] < target:
                left = mid + 1      # Search right half
            else:
                right = mid - 1     # Search left half
                
        # Target not found; left is the insert position
        return left

# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.searchInsert([1, 2, 3, 5], 4))  # Output: 3
