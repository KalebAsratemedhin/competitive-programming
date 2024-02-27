class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combo = []
        candidates.sort()
        def helper(num, start):
            if sum(combo) == target:
                ans.append(combo.copy())

            for i in range(start, len(candidates)):
                if num - candidates[i] >= candidates[i] or num - candidates[i] == 0:
                    combo.append(candidates[i])
                    helper(num - candidates[i], i )
                    combo.pop()

        helper(target, 0)
        return ans