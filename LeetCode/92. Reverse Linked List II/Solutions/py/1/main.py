# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: ListNode) -> (ListNode, ListNode):
        # n = len(head)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        previous_node = None
        tail = head
        while head:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node
        return previous_node, tail

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # n = len(head)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        dummy_head = ListNode(next=head)

        idx = 1
        curr = head
        prev_l = dummy_head
        head_to_reverse = head

        while idx <= right:
            if idx == left - 1:
                prev_l = curr
                head_to_reverse = curr.next
            elif idx == right:
                after_r = curr.next
                curr.next = None

            curr = curr.next
            idx += 1

        head_reversed, tail_reversed = self.reverseLinkedList(head_to_reverse)

        prev_l.next = head_reversed
        tail_reversed.next = after_r

        return dummy_head.next
