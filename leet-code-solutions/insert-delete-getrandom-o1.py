class RandomizedSet:

    def __init__(self):
        self.random = {}
        self.indices = {}
        self.index = 0

    def insert(self, val: int) -> bool:
        if val in self.random:
            return False
        self.random[val] = self.index
        self.indices[self.index] = val
        self.index += 1
        return True
    
    def remove(self, val: int) -> bool:
        if val in self.random:
            idx = self.random[val]
            v = self.indices[idx]
            if idx == self.index - 1:
                del self.indices[idx]
                del self.random[v]
            else:
                del self.indices[idx]
                del self.random[val]
                self.indices[idx] = self.indices[self.index - 1]
                self.random[self.indices[idx]] = idx
                del self.indices[self.index - 1]
            self.index -= 1
            
            return True
        return False        

    def getRandom(self) -> int:
        return self.indices.get(random.randint(0, self.index - 1))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()