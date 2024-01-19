class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        dict = {0 : 1}
        ans = 0
        for i in range(n):
            prefix += nums[i]
            if prefix - k in dict:
                ans += dict[prefix - k]        
            dict[prefix] = dict.get(prefix, 0) + 1

        return ans
