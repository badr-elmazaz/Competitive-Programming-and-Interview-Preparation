# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n = len(head)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        hashmap = {}
        
        node = head
        dummy_head = ListNode(next = head)
        hashmap[-1] = dummy_head
        idx = 0

        while node:
            hashmap[idx] = node
            idx += 1
            node = node.next

        idx_remove = idx - n

        prev, curr = hashmap[idx_remove - 1], hashmap[idx_remove]
        prev.next = curr.next

        return dummy_head.next
