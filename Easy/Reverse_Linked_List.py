class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node
        return prev
def printOutput(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
rev = sol.reverseList(head)
print(printOutput(rev))
