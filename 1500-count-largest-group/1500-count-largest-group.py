class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)

        for i in range(1, n + 1):
            count = 0
            for d in str(i):
                count += int(d)
            groups[count] += 1
        
        max_ = max(groups.values())
        ans = 0

        for key, val in groups.items():
            if val == max_:
                ans += 1
        return ans
