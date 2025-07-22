# Last updated: 7/22/2025, 3:23:09 PM
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        stack = []
        ans = []

        for i, num in enumerate(nums):

            if stack and num - stack[-1] != 1:
                stack = []

            stack.append(num)
            if i >= k - 1:
                if len(stack) >= k:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
        return ans


