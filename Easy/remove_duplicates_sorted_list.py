# File: remove_duplicates_sorted_list.py
# Problem: Remove Duplicates from Sorted List (LeetCode 83)
# Difficulty: Easy
# Description: Given the head of a sorted linked list, delete all duplicates such 
# that each element appears only once. Return the linked list sorted as well.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.head = None

    def deleteDuplicates(self, head):
        """
        Remove duplicates from a sorted linked list.
        :param head: ListNode
        :return: ListNode
        """
        self.head = head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return self.head

    def printResult(self):
        """
        Convert the linked list to a Python list for easy display.
        :return: list
        """
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

# -----------------------------
# Example usage
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    sol.deleteDuplicates(head)
    print(sol.printResult())  # Output: [1, 2, 3, 4]
