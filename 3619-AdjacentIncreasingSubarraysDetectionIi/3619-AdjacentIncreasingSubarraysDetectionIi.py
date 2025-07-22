# Last updated: 7/22/2025, 3:23:04 PM
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        '''
        1. go through nums from left and keep increasing stack.
        2. keep length of stack on a list
        3. go through nums from right and keep decreasing stack
        4. keep length of decreasing stack on list
        5. go through list containing length of stacks and take min 
        6. return the max of the values in step 5


        '''
        increasing = []
        decreasing = []
        lengths = []

        for i, num in enumerate(nums):
            if not increasing or increasing and increasing[-1] < num:
                increasing.append(num)
            else:
                increasing = [num]

            lengths.append(len(increasing))

        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            ans = max(ans, min(len(decreasing), lengths[i]))
            if not decreasing or decreasing and decreasing[-1] > nums[i]:
                decreasing.append(nums[i])
            else:
                decreasing = [nums[i]]

        
        return ans


            
