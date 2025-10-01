# Merge Two Sorted Linked Lists 🧩🔗✨
# Difficulty: Easy ✅

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Merge two sorted linked lists and return the merged sorted list.
        :param list1: ListNode
        :param list2: ListNode
        :return: ListNode
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

def to_list(head):
    """
    Convert linked list to Python list for easy visualization.
    :param head: ListNode
    :return: list
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage
if __name__ == "__main__":
    # Create first linked list: 1 -> 2 -> 4
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)

    # Create second linked list: 1 -> 3 -> 4
    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    # Merge lists
    solution = Solution()
    merged_head = solution.mergeTwoLists(node1, node2)

    # Convert merged list to Python list and print
    merged_list = to_list(merged_head)
    print(merged_list)
