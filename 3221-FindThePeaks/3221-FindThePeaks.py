# Last updated: 7/22/2025, 3:23:51 PM
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        for i in range(1, len(mountain)):
            if i < len(mountain) - 1:
                if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                    peaks.append(i)
        return peaks