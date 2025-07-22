# Last updated: 7/22/2025, 3:26:07 PM
class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_index = {}
        

    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number

        if number not in self.num_to_index:
            self.num_to_index[number] = []
        heapq.heappush(self.num_to_index[number], index)
        

    def find(self, number: int) -> int:
        if number not in self.num_to_index:
            return -1
        
        while self.num_to_index[number] and number != self.index_to_num[self.num_to_index[number][0]]:
            heapq.heappop(self.num_to_index[number])
        
        if self.num_to_index[number]:
            return self.num_to_index[number][0]
        
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)