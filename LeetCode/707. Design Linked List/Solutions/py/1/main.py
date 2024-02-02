class ListNode:

    def __init__(self, val: int, next_node: ListNode = None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length = 0
        
        

    def get(self, index: int) -> int:
        if index < 0 or index > self.length-1:
            return -1
        return self.get_node(index).val

    def get_node(self, index: int) -> ListNode:
        if index < 0 or index > self.length-1:
            return
        node = self.head
        for i in range(index):
            node = node.next
        return node

        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val=val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val=val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val=val)
        if index < 0 or index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        prev_node_to_shift = self.get_node(index-1)
        tmp = prev_node_to_shift.next
        prev_node_to_shift.next = new_node
        new_node.next = tmp
        self.length += 1

        

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length-1 or self.length < 1:
            return
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return
        if index == 0:
            tmp = self.head.next
            self.head.next = None
            self.head = tmp
            self.length -= 1
            return
        
        prev_node_to_delete = self.get_node(index-1)
        tmp = prev_node_to_delete.next.next
        prev_node_to_delete.next.next = None
        prev_node_to_delete.next = tmp

        if index == self.length-1:
            self.tail = prev_node_to_delete

        self.length -= 1
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)