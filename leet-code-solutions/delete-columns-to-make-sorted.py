class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        deletions = 0
        for i in range(len(strs[0])):
            prev = ord(strs[0][i])
            for j in range(n):
                if ord(strs[j][i]) < prev:
                    deletions += 1
                    break
                prev = ord(strs[j][i])
        return deletions
