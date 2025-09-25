class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                current_count = 0
            max_count = max(max_count, current_count)
        return max_count
obj = Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1,1,1]))