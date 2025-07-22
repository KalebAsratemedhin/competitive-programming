# Last updated: 7/22/2025, 3:26:17 PM
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict = {}
        for key, value in enumerate(nums):
            dict[value] = key

        for op in operations:
            nums[dict[op[0]]] = op[1]
            dict[op[1]] = dict[op[0]]
        
        return nums