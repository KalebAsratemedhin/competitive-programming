class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        output = []
        nums.sort()
        while i < len(nums):
            target = -(nums[i])
            j = i + 1
            k = len(nums) - 1
            if i != 0 and nums[k] == nums[i]:
                break
            while j < k:
                if nums[j] +  nums[k] < target:
                    j += 1
                elif nums[j] +  nums[k] > target:
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in output:
                        output.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
            i += 1
        return output
