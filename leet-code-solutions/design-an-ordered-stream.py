class OrderedStream:

    def __init__(self, n: int):
        self.list = [-1] * n
        self.pointer = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey - 1] = value
        if self.list[self.pointer] == -1:
            return []
        while self.pointer < self.n and self.list[self.pointer] != -1:
            self.pointer += 1
        
        return self.list[idKey - 1: self.pointer]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)