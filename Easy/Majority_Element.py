"""
Majority Element using Boyer-Moore Voting Algorithm

Problem:
Given an array nums, return the majority element (element appearing more than n/2 times).
Assume the majority element always exists.
"""

class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


if __name__ == "__main__":
    # Example usage
    nums1 = [3,2,3]
    nums2 = [2,2,1,1,1,2,2]
    
    obj = Solution()
    print("Majority element in {} is {}".format(nums1, obj.majorityElement(nums1)))  # Output: 3
    print("Majority element in {} is {}".format(nums2, obj.majorityElement(nums2)))  # Output: 2
