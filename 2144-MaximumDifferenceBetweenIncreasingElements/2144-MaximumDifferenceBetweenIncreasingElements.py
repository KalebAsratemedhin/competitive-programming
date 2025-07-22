# Last updated: 7/22/2025, 3:27:19 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        stack = []

        for num in nums:
            while stack and stack[-1] >= num:
                ans = max(ans, stack[-1] - stack[0])
                stack.pop()

            stack.append(num)

        if len(stack) >= 2:
            ans = max(ans, stack[-1] - stack[0])

        return ans if ans > 0 else -1
