class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mx = flips[0]
        flipped = 0
        aligned = 0
        for i in range(len(flips)):
            mx = max(flips[i], mx)
            flipped += 1
            if flipped == mx:
                aligned += 1

        return aligned