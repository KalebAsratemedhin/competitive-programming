class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = j = 0
        n = len(blocks)
        size = operations = 0
        ans = n
        while i < n and j < n:
            if blocks[j] == 'W':
                operations += 1
                size += 1
                j += 1
            else:
                size += 1
                j += 1
            if size == k:
                ans = min(ans, operations)
                if blocks[i] == 'W':
                    operations -= 1
                i += 1
                size -= 1
        return ans