# Last updated: 7/22/2025, 3:26:29 PM
class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int
    ) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break  
        return res