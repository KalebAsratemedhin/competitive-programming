class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.dummy = Node(0, self.head)
        self.tail = self.head
        self.length = 0
        

    def get(self, index: int) -> int:
     
        curr = self.dummy
        count = 0
        if index < self.length:
            while count <= index:
                curr = curr.next
                count += 1
            return curr.val
        else:
            return -1
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.length:
            curr = self.dummy
            new = Node(val)
            count = 0
            while count < index:
                curr = curr.next
                count += 1
            new.next = curr.next
            curr.next = new
            if index == 0:
                self.head = self.dummy.next
            if index == self.length:
                self.tail = curr.next
            self.length += 1
            
         

    def deleteAtIndex(self, index: int) -> None:
        count = 0
        if index < self.length:
            curr = self.dummy
            while count < index:
                curr = curr.next
                count += 1
            curr.next = curr.next.next
            if index == self.length - 1:
                self.tail = curr
            self.length -= 1
     

    def __str__(self) -> str:
        curr = self.dummy
        arr = []
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        

        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)