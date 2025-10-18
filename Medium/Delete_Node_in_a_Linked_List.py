class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def __init__(self, head=None):
        self.head = head

    def deleteNode(self, data): 
        # If list is empty
        if not self.head:
            return
        
        # If head node needs to be deleted
        if self.head.val == data:
            self.head = self.head.next
            return

        # Otherwise, find the node before the one to delete
        current = self.head
        while current.next:
            if current.next.val == data:
                current.next = current.next.next
                return
            current = current.next

def printOutput(head):
    output = []
    while head:
        output.append(head.val)
        head = head.next
    return output

# Create linked list: 10 -> 20 -> 30 -> 40
head = ListNode(10, ListNode(20, ListNode(30, ListNode(40))))
sol = Solution(head)
sol.deleteNode(10)
print(printOutput(sol.head))

