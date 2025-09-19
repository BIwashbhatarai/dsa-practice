# class Solution(object):
#     def missingNumber(self, nums):
#         n = len(nums)
#         sum_of_n_numbers = int((n*(n+1))/2)
#         sum_of_arr = sum(nums)
#         return sum_of_n_numbers - sum_of_arr
# obj = Solution()
# print(obj.missingNumber([0,1,3]))



class Solution(object):
    def missingNumber(self, nums):
        xor_all = 0
        xor_arr = 0
        
        for i in range(len(nums)+1):
            xor_all ^= i
        
        for num in nums:
            xor_arr ^= num
        
        return xor_all ^ xor_arr
obj = Solution()
print(obj.missingNumber([0,1,3]))