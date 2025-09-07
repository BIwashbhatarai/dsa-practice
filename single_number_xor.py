# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one using XOR with O(n) time and O(1) space.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize result variable
        result = 0
        
        # XOR all numbers. Duplicates cancel out, leaving the single number
        for num in nums:
            result ^= num
        
        return result

# Example usage
if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,2,3,3,4,4]
    print("Single number is:", obj.singleNumber(nums))
    # Output: Single number is: 1
