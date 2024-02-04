class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        ans=[]
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                ans.append(s[i])

        for i in range(len(s)):
            if not s[i].isalpha():
                ans.insert(i,s[i])
 
        return ''.join(ans)
       