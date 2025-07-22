# Last updated: 7/22/2025, 3:23:46 PM
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        curr = [nums[0]]

        for i in range(1, len(nums)):
            left = nums[i] - nums[i - 1]

            if nums[i] - curr[0] <= k and len(curr) < 3:
                curr.append(nums[i])
            else:
                if len(curr) != 3:
                    return []
                ans.append(curr)
                curr = [nums[i]]
        
        if curr:
            ans.append(curr)
        return ans

                

        

