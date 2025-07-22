# Last updated: 7/22/2025, 3:22:48 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odds, evens = [], []

        for key, val in cnt.items():
            if val & 1:
                odds.append(val)
            else:
                evens.append(val)
        
        return max(odds) - min(evens)