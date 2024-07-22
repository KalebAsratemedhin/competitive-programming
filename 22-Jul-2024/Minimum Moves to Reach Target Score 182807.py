# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if maxDoubles > 0:
                moves += 1
                moves += target % 2
                target = target // 2
                maxDoubles -= 1
            else:
                moves += target - 1
                return moves
                
        return moves

