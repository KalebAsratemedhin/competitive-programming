class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        remainders = {0 : 1}
        ans = 0
        prefix = 0
        for i in range(n):
            prefix += nums[i]
            rem = prefix % k
            ans += remainders.get(rem, 0)
            remainders[rem] = remainders.get(rem, 0) + 1
        return ans