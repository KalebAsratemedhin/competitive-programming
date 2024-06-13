# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wd1 = ""
        wd2 = ""
        for word in word1:
            wd1 += word
        for word in word2:
            wd2 += word
        return wd1 == wd2