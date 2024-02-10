# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # n = len(listnode)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        dummy_head = ListNode()
        dummy_head.next = head
        node = dummy_head

        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
    
        return dummy_head.next