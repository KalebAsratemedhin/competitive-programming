class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        bit_count = bin(k - 1).count('1')
        return bit_count & 1
             
