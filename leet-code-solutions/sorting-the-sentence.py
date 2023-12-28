class Solution(object):
    def sortSentence(self, s):
        arr = s.split(" ")
        for j in range(len(arr)):
            for i in range(len(arr) - 1 - j):
                if arr[i][-1] > arr[i + 1][-1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        final=""
        for i in range(len(arr)):
            word = ""
            for c in range(len(arr[i])-1):
                word += arr[i][c]
            if i < len(arr) - 1:
                word += " "
            final += word 
        return final