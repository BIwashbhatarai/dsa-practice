class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if n == length:
            return head.next
        current = head
        for _ in range(length - n - 1):
            current = current.next
        
        current.next = current.next.next
        return head

def printResult(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
remove = sol.removeNthFromEnd(head, 2)
print(printResult(remove))
        