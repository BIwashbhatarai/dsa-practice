# Problem: Roman to Integer
# LeetCode Link: https://leetcode.com/problems/roman-to-integer/
#
# Given a Roman numeral string, convert it to an integer.
# Roman numerals use subtraction in some cases (e.g., IV = 4, IX = 9).

class Solution(object):
    def romanToInt(self, s):
        # Mapping of Roman numerals to integers
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        n = len(s)

        # Loop through each character except the last
        for i in range(n - 1):
            if values[s[i]] < values[s[i + 1]]:
                # Subtract if smaller value is before a larger value
                total -= values[s[i]]
            else:
                # Otherwise, add the value
                total += values[s[i]]

        # Add the value of the last character
        total += values[s[-1]]

        return total

# --- Example Usage ---
if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("L"))        # Output: 50
    print(obj.romanToInt("III"))      # Output: 3
    print(obj.romanToInt("IV"))       # Output: 4
    print(obj.romanToInt("MCMXCIV"))  # Output: 1994
