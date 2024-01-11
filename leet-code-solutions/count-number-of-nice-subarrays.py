class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odds = {0 : 1}
        ans = 0
        count = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                count += 1
            odds[count] = odds.get(count, 0) + 1
            ans += odds.get(count - k, 0)
        return ans

