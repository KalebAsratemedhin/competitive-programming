class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        n = len(s)
        right = left = 0
        ans = 0
        while right < n:
            if s[right] not in window:
                window.add(s[right])
                right += 1
            else:
                window.remove(s[left])
                left += 1
            ans = max(ans, (right - left))
        return ans