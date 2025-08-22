"""
Title: Longest Common Prefix – Horizontal Scanning Approach
Description: This program finds the longest common prefix among a list of strings.
Author: Your Name
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix string amongst an array of strings.
        
        :param strs: List[str] - list of input strings
        :return: str - longest common prefix
        """
        if not strs:
            return ""
        
        # Take the first string as initial prefix
        prefix = strs[0]
        
        # Compare prefix with each string and shrink if necessary
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last character
                if prefix == "":
                    return ""  # no common prefix
        
        return prefix


if __name__ == "__main__":
    # Example usage
    strs = ["flower", "flow", "flight"]
    solution = Solution()
    print("Longest Common Prefix:", solution.longestCommonPrefix(strs))
