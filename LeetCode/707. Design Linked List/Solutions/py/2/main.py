class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        
        

    def get(self, index: int) -> int:
        node = self.get_node(index)
        return node.val if node else -1

    def get_node(self, index: int) -> Node:
        if index < 0:
            return
        current_node = self.head
        for i in range(index):
            if not current_node:
                break
            current_node = current_node.next
        return current_node

        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val=val)

        if self.head:
            new_node.next = self.head
        else:
            self.tail = new_node

        self.head = new_node        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val=val)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val=val)

        prev_node = self.get_node(index-1)

        if not prev_node:
            return

        if prev_node == self.tail:
            self.addAtTail(val)
            return

        tmp = prev_node.next
        prev_node.next = new_node
        new_node.next = tmp

        

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        prev_node = self.get_node(index-1)

        if not prev_node or prev_node == self.tail:
            return
        # remove tail
        if prev_node.next == self.tail:
            prev_node.next = None
            self.tail = prev_node
            return

            
        prev_node.next = prev_node.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)