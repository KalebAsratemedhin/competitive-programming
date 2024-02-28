class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        kth = float("-inf")
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < kth:
                return True
            while stack and nums[i] > stack[-1]:
                kth = stack.pop()
            stack.append(nums[i])
        return False
