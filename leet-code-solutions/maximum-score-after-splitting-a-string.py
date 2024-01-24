class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        counts = [0] * n
        ones = 0
        ans = 0
        for i in range(n):
            if i > 0:
                if s[i] == '0':
                    counts[i] += 1
                counts[i]+= counts[i - 1]
            elif s[i] == '0':
                counts[i] += 1
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                ones += 1
            if i > 0:
                ans = max(ans, ones + counts[i - 1])
        return ans
        
            