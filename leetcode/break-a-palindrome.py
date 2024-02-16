class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = (len(palindrome) // 2) + (len(palindrome) % 2)
        changed = False
        ans = list(palindrome)
        
        if len(palindrome) == 1:
            return ""

        for i in range(n):
            if ord(palindrome[i]) > ord('a') and not changed:
                if i != n - 1 or palindrome[i + 1] != "a":
                    ans[i] = ("a")
                    changed = True 
    
        if not changed:
            ans[-1] = "b"

        return "".join(ans)




