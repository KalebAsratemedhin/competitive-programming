# Last updated: 7/22/2025, 3:27:36 PM
class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        cursor = ord('a')
        for i in range(len(word)):
            if ord(word[i]) == cursor:
                time += 1
            else:
                cost = abs(cursor - ord(word[i]))
                time += min(cost, 26 - cost) + 1
                cursor = ord(word[i])
        return time