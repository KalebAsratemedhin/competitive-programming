# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        numMoves, sum = 0, 0

        while sum < target or (sum - target) & 1:
            numMoves += 1
            sum += numMoves

        return numMoves
