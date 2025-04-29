class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = ans = 0
        max_ = max(nums)
        left = nums.index(max_)

        for i in range(len(nums)):
            if nums[i] == max_:
                count += 1


            if count > k:
                left += 1
                count -= 1
                while nums[left] != max_:
                    left += 1

            if count == k:
                ans += 1 + left

        return ans


