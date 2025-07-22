# Last updated: 7/22/2025, 3:24:11 PM
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        if len(str2) > len(str1):
            return False
        first = 0
        for second in range(len(str2)):
            while first < len(str1) and str2[second] not in {str1[first], chr((ord(str1[first]) - ord('a') + 1) % 26 + ord('a')) }:
                
                first += 1

            if first < len(str1):
                print({str1[first], chr((ord(str1[first]) - ord('a') + 1) % 26 + ord('a')) }, str1[first], str2[second])

            if first < len(str1) and str2[second] in {str1[first], chr((ord(str1[first]) - ord('a') + 1) % 26 + ord('a')) }:
                first += 1
            else:
                return False
            

        return True
