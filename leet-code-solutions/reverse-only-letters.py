class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        u=s[::-1]
        l=[]
        for i in range(len(u)):
            if u[i].isalpha():
                l.append(u[i])
        for i in range(len(s)):
            if not s[i].isalpha():
                l.insert(i,s[i])
        p = ''.join(l)
        return p
       