class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def is_valid(first, second):
            curr, nxt = words[first], words[second]
            if groups[first] == groups[second] or len(curr) != len(nxt):
                return False
            cnt = 1
            for i in range(len(curr)):
                if curr[i] != nxt[i]:
                    if cnt:
                        cnt -= 1
                    else:
                        return False
            return True
        
        n = len(words)
        @cache
        def dp(prev, ind):
            if ind >= n:
                return []

            ans = []
            if is_valid(prev, ind):
                new = [words[ind]] + dp(ind, ind + 1)
                if len(new) > len(ans):
                    ans = new

            new = dp(prev, ind + 1)
            if len(new) > len(ans):
                ans = new
        
            return ans

        ans = []
        for i in range(n):
            new = [words[i]] + dp(i, i)
            if len(new) > len(ans):
                ans = new

        return ans
