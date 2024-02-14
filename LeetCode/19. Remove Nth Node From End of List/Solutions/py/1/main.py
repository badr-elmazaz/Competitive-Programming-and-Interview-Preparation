# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n = len(head)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        size = 0

        node = head

        while node:
            node = node.next
            size += 1

        idx_remove = size - n

        dummy_node = ListNode(next = head)

        prev, curr = dummy_node, head
        idx = 0 

        while idx <= idx_remove:
            if idx == idx_remove:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            idx += 1

        return dummy_node.next