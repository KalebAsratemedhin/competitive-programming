# Last updated: 7/22/2025, 3:27:28 PM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def add_one(curr):
            for i in range(len(curr) - 1, -1, -1):
                if curr[i] == '0':
                    curr[i] = '1'
                    return "".join(curr)
                curr[i] = '0'
            return ''
            
        def subtract_one(curr):
            for i in range(len(curr) - 1, -1, -1):
                if curr[i] == '1':
                    curr[i] = '0'
                    return "".join(curr)
                curr[i] = '0'
            return ''

        nums_set = set(nums)
        for num in nums:
            curr = [c for c in num]

            next_num = add_one(curr.copy())
            prev_num = subtract_one(curr.copy())

            if next_num and next_num not in nums_set:
                return next_num
            if prev_num and prev_num not in nums_set:
                return prev_num

        
            