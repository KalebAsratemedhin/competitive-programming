class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = Counter(s)
        evens = 0
        odds = 0
        for key, value in map.items():
            evens += (value // 2) * 2
            odds += value % 2
        if odds:
            return evens + 1
        return evens

