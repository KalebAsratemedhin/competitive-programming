class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(s):
            if len(s) <= 1:                
                return ""

            st = set(s)

            for i in range(len(s)):
                if s[i].swapcase() not in st:
                    left = helper(s[:i])
                    right = helper(s[i + 1:])
                    if len(left) >= len(right):
                        return left
                    else:
                        return right
            return s
        return helper(s)

