# Last updated: 7/22/2025, 3:25:17 PM
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(" ")

        for i in range(1, len(arr)):
            if arr[i][0] != arr[i - 1][-1]:
                return False
        
        if arr[0][0] == arr[-1][-1]:
            return True
        
        return False

