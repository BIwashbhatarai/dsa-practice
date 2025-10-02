class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]
    
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
isPalindrome = sol.isPalindrome(head)
print(isPalindrome)