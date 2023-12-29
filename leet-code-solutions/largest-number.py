class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p1 = str(nums[i])+ str(nums[j])
                p2 = str(nums[j])+ str(nums[i])
                if int(p2) > int(p1):
                    nums[i], nums[j] = nums[j], nums[i]
        ans = ""
        for n in nums:
            if n == 0 and len(ans) == 0:
                continue
            ans += str(n)
        if len(ans) == 0:
            return "0"
        return ans


