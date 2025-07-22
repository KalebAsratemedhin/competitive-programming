# Last updated: 7/22/2025, 3:23:45 PM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = {}
        maxima = 0
        for key, value in freq.items():
            maxima = max(value, maxima)
            if value in max_freq:
                max_freq[value] += value
            else:
                max_freq[value] = value
        return max_freq[maxima]
            