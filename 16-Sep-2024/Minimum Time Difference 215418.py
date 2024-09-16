# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = [tuple(map(int, time.split(':'))) for time in timePoints]
        arr.sort()

        arr.append(arr[0])
        ans = float('inf')

        for i in range(1, len(arr)):
            hour_i, minutes_i = arr[i - 1]
            hour_f, minutes_f = arr[i]
            
            diff = abs((hour_f - hour_i) * 60 + minutes_f - minutes_i)
            ans = min(ans, diff, (24 * 60 - diff))

        return ans

