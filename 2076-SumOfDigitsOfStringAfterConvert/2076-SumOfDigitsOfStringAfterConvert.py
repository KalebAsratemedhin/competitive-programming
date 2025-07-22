# Last updated: 7/22/2025, 3:27:37 PM
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = 0
        arr = []
        for c in s:
            arr.append(str(ord(c) - ord('a') + 1))
            
        num = int("".join(arr))
        for i in range(k):
            temp = str(num)
            num = 0
            for c in temp:
                num += int(c)
        return num

