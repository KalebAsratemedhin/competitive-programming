class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        over = False
        common = len(strs[0])
        for i in range(common):
            target = strs[0][i]
            for s in strs:
                if i >= len(s):
                    over = True
                elif s[i] != target:
                    over = True
                    break
            if not over:
                ans += s[i] 
            if over:
                break
            
        return ans


