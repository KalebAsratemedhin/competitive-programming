# Last updated: 7/22/2025, 3:24:57 PM
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        large = 0
        ans = []
        sum = 0
        for num in nums:
            large = max(num, large)
            sum += num + large
            ans.append(sum)
        return ans
    