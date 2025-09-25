class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        nums_set = set(nums)
        missing_num = []
        for i in range(1 , n+1):
            if i not in nums_set:
                missing_num.append(i)
        return missing_num
obj = Solution()
print(obj.findDisappearedNumbers( [4,3,2,7,8,2,3,1]))