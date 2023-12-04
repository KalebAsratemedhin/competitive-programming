class Solution:
    def printVertically(self, s: str) -> List[str]:
        n = len(s)
        lst = s.split()
        ans = []
        m = 0
        for word in lst:
            m = max(m, len(word))

        for j in range(m):
            a = ""
            for word in lst:
                if j < len(word):
                    a += word[j]
                else:
                    a += " "

                    
            ans.append(a.rstrip())
        return ans
                

