"""
Valid Palindrome Checker

Check if a given string is a palindrome by:
1. Converting all letters to lowercase.
2. Removing all non-alphanumeric characters.
3. Comparing the cleaned string with its reverse.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if the string s is a palindrome.
        
        Args:
            s (str): Input string
        
        Returns:
            bool: True if s is a palindrome, False otherwise
        """
        s = s.lower()  # Convert to lowercase
        cleaned = ''
        
        # Keep only letters and numbers
        for char in s:
            if char.isalnum():
                cleaned += char

        # Check palindrome
        return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # Testing examples
    obj = Solution()
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(obj.isPalindrome("race a car"))                      # False
    print(obj.isPalindrome(" "))                               # True
    print(obj.isPalindrome("mam"))                             # True
