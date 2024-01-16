# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n = num_all_nodes
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        linked_list_length = 0

        node = head

        while node:
            linked_list_length += 1
            node = node.next
        
        middle_idx = linked_list_length // 2

        node = head
        current_idx = 0
        
        while node:
            if current_idx == middle_idx:
                return node
            node = node.next
            current_idx += 1
