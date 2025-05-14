class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        def op(mp):
            new = [0] * 26
            for i in range(26):
                for j in range(nums[i]):
                    new[(i + j + 1) % 26] += mp[i]
            return [x % mod for x in new]

        @cache
        def dfs(i, t):
            res = [0] * 26
            if t == 0:
                res[i] = 1
                return res

            half = dfs(i, t // 2)
            for j in range(26):
                new = dfs(j, t // 2)
                for k in range(26):
                    res[k] += half[j] * new[k] % mod
            if t % 2 == 1:
                res = op(res)
            return res
        
        return sum(sum(dfs(ord(c) - ord('a'), t)) for c in s) % mod

