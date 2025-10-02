class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, data):
        while head and head.val == data:
            head = head.next
            
        current = head
        while current and current.next:
            if current.next.val == data:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
def printOutput(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


sol = Solution()
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
removeEl = sol.removeElements(head, 6)
print(printOutput(removeEl))
                
        