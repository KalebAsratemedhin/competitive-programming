class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        min_len = min(len(word1), len(word2))
        i = j = 0
        for k in range(2 * min_len):
            if k % 2 == 0:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
        while i < len(word1):
            ans += word1[i]
            i += 1
        while j < len(word2):
            ans += word2[j]
            j += 1
        return ans