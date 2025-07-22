# Last updated: 7/22/2025, 3:24:30 PM
class Solution:
    def minLength(self, s: str) -> int:
        while s:
            i = s.find('AB')
            j = s.find('CD')

            if i == -1 and j == -1:
                return len(s)

            elif i == -1:
                s = s[:j] + s[j + 2:]
            elif j == -1:
                s = s[:i] + s[i + 2:]
            elif i < j:
                s = s[:i] + s[i + 2: j] + s[j + 2:]
            else:
                s = s[:j] + s[j + 2: i] + s[i + 2:]
            


        return len(s)

        

            

