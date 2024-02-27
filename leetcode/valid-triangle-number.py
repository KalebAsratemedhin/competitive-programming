class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        triplets =0
        for i in range(n - 1, -1, -1):
            a = nums[i]
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > a:
                    triplets += (r - l)
                    r -= 1
                else:
                    l += 1
                        
        return triplets