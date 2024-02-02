# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add_value(self, head, value):
        if head.val is None:
            head.val = value
            return head
        node = ListNode(val=value)
        head.next = node
        head = head.next
        return head


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        head = ListNode(val=None)
        h = head

        while list1 or list2:
            if (list1 and not list2) or (list1.val < list2.val):
                head.next = list1
                list1 = list1.next
            elif (list2 and not list1) or (list1.val > list2.val):
                new_value = list2.val
                head = self.add_value(head, new_value)
                list2 = list2.next
            elif list1.val == list2.val:
                new_value = list1.val
                head = self.add_value(head, new_value)
                list1 = list1.next
                head = self.add_value(head, new_value)
                list2 = list2.next

        return h


        