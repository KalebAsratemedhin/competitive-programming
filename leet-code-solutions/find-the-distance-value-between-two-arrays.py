class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num in arr1:
            m = 0
            for y in arr2:
                if abs(y-num) <= d:
                    m += 1
            if m >= 1:
                count +=1
        return len(arr1) - count