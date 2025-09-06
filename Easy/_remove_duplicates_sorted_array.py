"""
26. Remove Duplicates from Sorted Array

Given a sorted integer array, remove the duplicates in-place such that 
each unique element appears only once. Return the number of unique elements 
k, and modify the first k elements of the array to be the unique elements 
in the original order.

Example:
    Input: nums = [1,1,2,3,4,4,5]
    Output: k = 5, nums = [1,2,3,4,5,_,_]
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array in-place.
        
        Args:
            nums (List[int]): Sorted input array.
        
        Returns:
            int: Number of unique elements.
        """
        if not nums:
            return 0

        i = 0  # Pointer for the last unique element

        # Iterate through the array starting from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1
                nums[i] = nums[j]

        return i + 1  # Total number of unique elements


if __name__ == "__main__":
    # Example usage
    obj = Solution()
    nums = [1, 1, 2, 3, 4, 4, 5]
    k = obj.removeDuplicates(nums)
    
    print("Number of unique elements:", k)          # Output: 5
    print("Array after removing duplicates:", nums[:k])  # Output: [1, 2, 3, 4, 5]
