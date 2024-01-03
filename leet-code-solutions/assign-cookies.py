class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0
        s.sort()
        g.sort()
        content = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1
            
        return content
            
              