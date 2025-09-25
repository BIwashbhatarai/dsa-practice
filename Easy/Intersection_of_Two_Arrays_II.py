from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        counts = Counter(nums1)
        res = []
        for n in nums2:
            if counts[n] > 0:
                res.append(n)
                counts[n] -= 1
        return res
