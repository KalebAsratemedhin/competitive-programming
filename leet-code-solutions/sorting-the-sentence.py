class Solution:
    def sortSentence(self, s: str) -> str:
        arr = sorted(s.split(" "), key = lambda x: int(x[-1]))
        ans = []
        for word in arr:
            ans.append(word[:-1])
        return " ".join(ans)
