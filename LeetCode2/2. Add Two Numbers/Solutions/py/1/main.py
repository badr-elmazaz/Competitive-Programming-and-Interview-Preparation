# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # n = len(l1)
        # m = len(l2)
        # Time Complexity:  O(max(n, m))
        # Space Complexity: O(max(n, m))

        carry = 0 
        
        node1 = l1 
        node2 = l2 
        
        result = ListNode() 
        head_result = result
        tail_result = result
        
        while node1 or node2:
          val1 = node1.val if node1 else 0 
          val2 = node2.val if node2 else 0 
          
          sum_val = val1 + val2 + carry
          carry = 0 if sum_val < 10 else 1 
          result = ListNode(val = sum_val % 10) 
          tail_result.next = result
          tail_result = result 
          
          node1 = node1.next if node1 else None
          node2 = node2.next if node2 else None
          
        if carry:
          result = ListNode(val = 1)
          tail_result.next = result        
        
        return head_result.next