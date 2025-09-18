class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        max_sum = 0
        i = 0 
        while i < len(nums):
            max_sum += min(nums[i] , nums[i + 1])
            i += 2
        return max_sum
obj = Solution()
print(obj.arrayPairSum([1,2,3,4]))