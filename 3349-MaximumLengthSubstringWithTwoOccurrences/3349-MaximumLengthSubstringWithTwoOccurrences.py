# Last updated: 7/22/2025, 3:23:32 PM
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, count = 0, 0
        window = {}

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            
            while window[s[right]] > 2:
                window[s[left]] -= 1
                left += 1
            count = max(count, right - left + 1)
        return count