class Solution(object):
    def moveZeroes(self, nums):
        current_pos = 0
        for num in nums:
            if num != 0:
                nums[current_pos] = num
                current_pos += 1
        while current_pos < len(nums):
            nums[current_pos] = 0
            current_pos += 1
            
obj = Solution()
nums =  [0, 2, 0, 1, 0]
obj.moveZeroes(nums)
print(nums)