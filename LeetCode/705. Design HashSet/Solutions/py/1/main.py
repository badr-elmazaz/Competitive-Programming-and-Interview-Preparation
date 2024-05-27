class ListNode:

    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.MAX = 10000
        self.hashset = [ListNode() for _ in range(self.MAX)]

    def add(self, key: int) -> None:
        idx = key % self.MAX
        node = self.hashset[idx]
        new_node = ListNode(val=key)

        while node.next:
            node = node.next
            if node.val == key:
                return
        node.next = new_node

    def remove(self, key: int) -> None:
        idx = key % self.MAX
        dummy_head = self.hashset[idx]
        prev, curr = dummy_head, dummy_head.next

        while curr:
            if curr.val == key:
                prev.next = curr.next
                break
            prev, curr = curr, curr.next

    def contains(self, key: int) -> bool:
        idx = key % self.MAX
        dummy_head = self.hashset[idx]
        node = dummy_head.next

        while node:
            if node.val == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
