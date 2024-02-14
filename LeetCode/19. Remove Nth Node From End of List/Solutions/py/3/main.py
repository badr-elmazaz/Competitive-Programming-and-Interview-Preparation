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
        

        dummy_head = ListNode(next = head)
        left = dummy_head
        right = dummy_head

        # bring right to n+1
        while n + 1:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy_head.next


