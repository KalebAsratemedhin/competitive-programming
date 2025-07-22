# Last updated: 7/22/2025, 3:26:36 PM
class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.counts = 0
        self.arr = ['0'] * size
        self.flipped = ['1'] * size

    def fix(self, idx: int) -> None:
        if self.arr[idx] == '0':
            self.counts += 1
        self.arr[idx] = '1'
        self.flipped[idx] = '0'
        
    def unfix(self, idx: int) -> None:
        if self.arr[idx] == '1':
            self.counts -= 1
        self.arr[idx] = '0'
        self.flipped[idx] = '1'

    def flip(self) -> None:
        self.counts = self.size - self.counts
        self.arr, self.flipped = self.flipped, self.arr

    def all(self) -> bool:
        return self.counts == self.size   
    
    def one(self) -> bool:
        return self.counts >= 1

    def count(self) -> int:
        return self.counts

    def toString(self) -> str:
        return "".join(self.arr)
        
    

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()