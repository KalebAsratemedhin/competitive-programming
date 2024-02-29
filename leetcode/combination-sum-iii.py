class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        arr = []
        def helper(start):
            if len(arr) == k and sum(arr) == n:
                ans.append(arr.copy())

            for i in range(start, 10):
                if sum(arr) > n:
                    continue
                arr.append(i)
                helper(i + 1)
                arr.pop()

        helper(1)
        return ans
