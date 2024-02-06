class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cs = []
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                cs.append(i)
        for i in range(len(s)):
            dist = abs(i - cs[0])
            for j in cs:
                if abs(i - j) > dist:
                    break
                dist = min(dist, abs(i - j))
            ans.append(dist)
        return ans


