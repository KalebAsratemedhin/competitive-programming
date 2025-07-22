# Last updated: 7/22/2025, 3:25:03 PM
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        s = str(n)
        for i in range(len(s)):
            if i % 2 == 0:
                ans += int(s[i])
            else:
                ans -= int(s[i])
        return ans

