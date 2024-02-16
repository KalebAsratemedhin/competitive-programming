class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0
        for i in s:
            if i == "(":
                opened += 1
            else:
                if opened:
                    opened -= 1
                else:
                    closed += 1
        return opened + closed