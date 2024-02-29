class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []
        candidates.sort()
        def helper(start):
            if sum(arr) == target:
                ans.append(arr.copy())
            for i in range(start, len(candidates)):
                if sum(arr) > target:
                    return
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                helper(i + 1)
                arr.pop()
        helper(0)

        return ans