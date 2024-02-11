class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return []
        start = nums[0]
        
        end = start
        for i in range(1,len(nums)):
            if nums[i - 1] == nums[i] - 1:
                end += 1
            else:
                ans.append([start, end])
                start = nums[i]
                end = start
        
        ans.append([start, end])

        for i in range(len(ans)):
            if  ans[i][0] == ans[i][1]:
                ans[i] = str(ans[i][0])
            else:
                ans[i] = f"{ans[i][0]}->{ans[i][1]}"
        return ans

