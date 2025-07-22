# Last updated: 7/22/2025, 3:24:43 PM
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            negs = k - (numOnes + numZeros)
            return numOnes - negs
