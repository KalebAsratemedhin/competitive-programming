class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = 0
        ans = 0
        zeros = 0
        while j < n:
            if nums[j] == 0:
                zeros += 1
            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1 

        return ans
