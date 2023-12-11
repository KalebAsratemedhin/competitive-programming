class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        n = len(arr)
        for key, value in counter.items():
            if value > n / 4:
                return key