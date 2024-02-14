class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        prefix = 0
        index = 0
        count = 0
        m = len(nums)
        i = 1
        
        while i <= n:
            if index < m and nums[index] <= i :
                prefix += nums[index]
                index += 1
                i = prefix
            elif i > prefix:
                count += 1
                prefix += i
                i = prefix
            else:
                i += 1

        return count


