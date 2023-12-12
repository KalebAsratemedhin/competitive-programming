class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.strip().split(" ")
        ans = []
        for word in s_arr:
            if len(word) != 0:
                ans.append(word)
        return " ".join(ans[:: -1])

            
