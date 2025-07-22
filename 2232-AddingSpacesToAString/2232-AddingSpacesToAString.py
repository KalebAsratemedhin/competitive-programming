# Last updated: 7/22/2025, 3:26:52 PM
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i, j = 0, 0
        ans = []

        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                ans.append(" ")
                j += 1
            ans.append(s[i])
        
        return "".join(ans)
