class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        arr = []
        def helper(start):
            if len(arr) == k:
                ans.append(arr.copy())
                return
            for i in range(start + 1, n + 1):
                if len(arr) + n + 1 - start >= k:
                    arr.append(i)
                    helper(i)
                    arr.pop()
            
        helper(0)
        return ans


