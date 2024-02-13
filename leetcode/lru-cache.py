class ListNode:
    def __init__(self, val = 0, key= 0, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

    def __str__(self):
        curr = self
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return str(arr)



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = self.head

    def addToTail(self, node):
        if self.tail == self.head:
            print("adding to head")
            self.head.next = node
            node.prev = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
        self.tail = node
    
    def removeNode(self, node):
        
        if node == self.tail:
            node.prev.next = node.next
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev


    def get(self, key: int) -> int:
        
        if key in self.map:
            self.removeNode(self.map[key])
            self.addToTail(self.map[key])
            return self.map[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.removeNode(node)
            self.addToTail(node)
            self.map[key].val = value
        else:
            new_node = ListNode(value, key)
            self.map[key] = new_node
            if self.capacity == 0:
                node = self.head.next
                if node.key in self.map:
                    del self.map[node.key]
                self.removeNode(node)
                self.capacity += 1
            self.addToTail(new_node)
            self.capacity -= 1
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)