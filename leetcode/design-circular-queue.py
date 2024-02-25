class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = self.head
        self.length = 0
        self.size = k
        
    def enQueue(self, value: int) -> bool:
        if self.length < self.size:
            new = ListNode(value)
            self.tail.next = new
            new.next = self.head
            self.tail = new
            self.length += 1
            return True

    def deQueue(self) -> bool:
        if self.length == 1:
            self.head.next = None
            self.tail = self.head
            self.length -= 1
            return True

        if self.length > 1:
            temp = self.head.next.next
            self.head.next.next = None
            self.head.next = temp
            self.length -= 1
            return True
        

    def Front(self) -> int:
        if self.length < 1:
            return -1
        return self.head.next.val
        

    def Rear(self) -> int:
        if self.length < 1:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()