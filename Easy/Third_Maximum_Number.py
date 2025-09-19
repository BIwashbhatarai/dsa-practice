class Solution(object):
    def thirdMax(self, nums):
        # Step 1: Remove duplicates
        unique_nums = set(nums)
        
        # Step 2: Initialize top 3 variables
        first_max = None
        second_max = None
        third_max = None
        
        # Step 3: Loop through unique numbers
        for num in unique_nums:
            if first_max is None or num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max is None or num > second_max:
                third_max = second_max
                second_max = num
            elif third_max is None or num > third_max:
                third_max = num
        
        # Step 4: Return result
        if third_max is None:
            return first_max
        else:
            return third_max

# Example usage
obj2 = Solution()
print("Solution 2 Output:", obj2.thirdMax([2, 2, 3, 1]))  # Output: 1
print("Solution 2 Output:", obj2.thirdMax([1, 2]))        # Output: 2
