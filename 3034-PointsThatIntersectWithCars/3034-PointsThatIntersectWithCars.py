# Last updated: 7/22/2025, 3:24:10 PM
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr = []
        for num in nums:
            arr += list(range(num[0], num[1] + 1))
        points = set(arr)
        return len(points)