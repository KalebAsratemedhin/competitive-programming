class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cost = 0
        possible = True
        prev = nums[0]
        for i in range(1, n):
            if nums[i] >= prev:
                prev = nums[i]
            else:
                cost += 1
            if cost > 1: 
                possible = False
        if possible:
            return True
        prev = nums[n - 1]
        cost = 0
        for i in range(n - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                cost += 1
            if cost > 1: 
                return False
        return True

            