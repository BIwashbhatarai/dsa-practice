class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.strip().split(" ")
        return len(word[-1])
obj = Solution()
print(obj.lengthOfLastWord("luffy is still joyboy"))