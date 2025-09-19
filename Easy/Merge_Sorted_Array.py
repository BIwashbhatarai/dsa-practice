class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)
# Test
obj = Solution()
nums1 = [1,2,3]
m = 3
nums2 = [4,5,6]
n = 3
obj.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,3,4,5,6]
