class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
obj = Solution()
print(obj.findNumbers([555,901,482,1771]))

# --------------- solution 2 -------------
class Solution(object):
    def findNumbers(self, nums):
        even_numbers = list(filter(lambda x: len(str(x)) % 2 == 0, nums))
        return len(even_numbers)
        
obj = Solution()
print(obj.findNumbers([555,901,482,1771]))