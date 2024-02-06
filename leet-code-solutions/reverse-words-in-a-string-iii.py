class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        s = s.split()
        for word in s:
            ans.append(word[::-1])
        return " ".join(ans)
    