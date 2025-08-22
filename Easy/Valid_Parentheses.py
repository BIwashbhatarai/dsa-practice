# Title: Valid Parentheses Checker Using Stack
# Description: This program checks if a given string containing only
# parentheses '()', '{}', '[]' is valid (balanced and correctly ordered).

class Solution:
    """
    Solution to check if a string of parentheses is valid using stack.
    """

    def isValid(self, s: str) -> bool:
        """
        Check if the input string s has valid parentheses.

        Args:
        s (str): Input string containing '()', '{}', '[]'.

        Returns:
        bool: True if valid, False otherwise.
        """
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in closeToOpen:  # closing bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:  # opening bracket
                stack.append(char)

        return not stack  # True if all matched, False otherwise


# Example usage
if __name__ == "__main__":
    obj = Solution()
    test_cases = ["({[]})", "(())", "()[]{}", "(]", "([])", "([)]"]
    for case in test_cases:
        print(f"{case} -> {obj.isValid(case)}")
