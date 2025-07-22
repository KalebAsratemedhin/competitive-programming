# Last updated: 7/22/2025, 3:24:08 PM
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        ans = []
        for i in range(len(s) - 1):
            if ones > 1:
                ans.append("1")
                ones -= 1
            else:
                ans.append("0")
        ans.append("1")
        return "".join(ans) 