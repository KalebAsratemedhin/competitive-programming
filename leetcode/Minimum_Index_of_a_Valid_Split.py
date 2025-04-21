class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dict = {}
        dominant = nums[0]
        for i in range(n):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
            if dict[nums[i]] > dict[dominant]:
                dominant = nums[i]
        size = 0
        count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                size += 1
                count += 1
                if count * 2 > size and (dict[dominant] - count) * 2 > (n - size):
                    return i