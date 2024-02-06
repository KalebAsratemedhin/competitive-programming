class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        filler = 0
        c_end = 0
        prev = -1
        n = len(s)

        while c_end < n:
            if s[c_end] != c:
                c_end += 1
            else:
                if prev == -1:
                    prev = c_end
                while filler <= c_end:
                    ans.append(min(abs(c_end - filler), abs(prev - filler) ))
                    filler += 1
                prev = c_end
                c_end += 1
        while filler < c_end:
            ans.append(abs(prev - filler))
            filler += 1
                
        return ans


