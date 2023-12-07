class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = []
        for r in ranges:
            arr += list(range(r[0], r[1] + 1))
        nums = set(arr)
        for i in range(left, right + 1):
            if i in nums:
                nums.remove(i)
            else:
                return False
        return True
