# 11. Container With Most Water
# LeetCode Problem Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
#
# Problem Statement:
# You are given an integer array `height` of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container 
# contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Constraints:
# - n == height.length
# - 2 <= n <= 10^5
# - 0 <= height[i] <= 10^4
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Example 2:
# Input: height = [1,1]
# Output: 1

class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# ✅ Example Usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected output: 49
    print(obj.maxArea([1,1]))                # Expected output: 1
