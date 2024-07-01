# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        high = position[-1]
        low = 0

        def testDistance(dist, m):
            balls = m - 1
            curr = position[0]
            for pos in position:
                if pos - curr >= dist:
                    balls -= 1
                    curr = pos
                if balls == 0:
                    return True
            return False


        while low < high:
            mid = (low + high) // 2

            if testDistance(mid, m):
                low = mid + 1
            else:
                high = mid
        return low - 1



