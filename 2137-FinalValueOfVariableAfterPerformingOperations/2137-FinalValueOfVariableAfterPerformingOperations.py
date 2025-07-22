# Last updated: 7/22/2025, 3:27:21 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:

            if op.find("+") != -1:
                x += 1
            else:
                x -= 1
        return x