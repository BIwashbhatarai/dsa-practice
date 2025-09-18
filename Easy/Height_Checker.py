class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
obj = Solution()
print(obj.heightChecker([1,5,4,3,2]))