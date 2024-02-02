# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n = num_all_nodes
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        hashtable = {}

        position = 0
        node = head

        while node:
            hashtable[position] = node
            node = node.next
            position += 1

        middle_position = position // 2

        return hashtable[middle_position]
        