class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        ans = list(s)

        while left < right:
            if ord(ans[left]) < ord(ans[right]):
                ans[right] = ans[left]
            elif ord(ans[left]) > ord(ans[right]):
                ans[left] = ans[right]
            left += 1
            right -= 1
            
        return "".join(ans)