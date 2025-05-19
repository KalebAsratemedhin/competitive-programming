class Solution:
    def triangleType(self, nums: List[int]) -> str:
        ans = {
            1: "equilateral",
            2: "isosceles",
            3: "scalene"
        }

        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"

        return ans[len(set(nums))]