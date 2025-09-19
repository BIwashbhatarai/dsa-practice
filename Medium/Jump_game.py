class Solution(object):
    def canJump(self, nums):
        maxReach = 0  # maximum index we can reach
        
        for i in range(len(nums)):
            if i > maxReach:
                return False  # cannot reach this index
            maxReach = max(maxReach, i + nums[i])
        
        return True  # last index is reachable

# Example usage
obj = Solution()
print(obj.canJump([2,3,1,1,4]))  # Output: True
print(obj.canJump([3,2,1,0,4]))  # Output: False