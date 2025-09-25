
class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for num in nums:
            ans.append(num)
        return nums + ans
obj = Solution()
print(obj.getConcatenation([1,2,1]))