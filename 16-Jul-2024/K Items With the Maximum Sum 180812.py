# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            negs = k - (numOnes + numZeros)
            return numOnes - negs
