# LeetCode 27: Remove Element
# Given an array nums and a value val, remove all occurrences of val in-place
# and return the new length of the array.

class Solution:
    def removeElement(self, nums, val):
        """
        Removes all occurrences of val in nums in-place.
        Returns the number of elements not equal to val.
        """
        count = 0  # Pointer for the next position of a valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]  # Place valid element at the front
                count += 1
        return count

# Example usage
if __name__ == "__main__":
    obj = Solution()
    arr = [1, 2, 3, 4, 5]
    val = 2
    k = obj.removeElement(arr, val)
    
    print("Number of elements left:", k)
    print("Array after removal:", arr[:k])  # Only print the valid part
