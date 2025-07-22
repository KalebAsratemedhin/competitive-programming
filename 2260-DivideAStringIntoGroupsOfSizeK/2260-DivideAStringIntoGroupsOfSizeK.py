# Last updated: 7/22/2025, 3:26:46 PM
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans, curr = [], []

        for c in s:
            curr.append(c)
            if len(curr) >= k:
                ans.append("".join(curr))
                curr = []
        
        if not curr:
            return ans

        for i in range(k - len(curr)):
            curr.append(fill)
        ans.append("".join(curr))

        return ans            