class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.occurence = {}

    def add(self, number: int) -> None:
        if number in self.freq and self.freq[number] in self.occurence:
            self.occurence[self.freq[number]] -= 1
            if self.occurence[self.freq[number]] == 0:
                del self.occurence[self.freq[number]]
        self.freq[number] = self.freq.get(number, 0) + 1
        self.occurence[self.freq[number]] = self.occurence.get(self.freq[number], 0) + 1
        
    def deleteOne(self, number: int) -> None:
        if number in self.freq and self.freq[number] in self.occurence:
            self.occurence[self.freq[number]] -= 1
            if self.occurence[self.freq[number]] == 0:
                del self.occurence[self.freq[number]]
            self.freq[number] -= 1
            if self.freq[number] == 0:
                del self.freq[number]
            if number in self.freq:
                self.occurence[self.freq[number]] = self.occurence.get(self.freq[number], 0) + 1
            
            
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.occurence:
            return True
        return False
        
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)