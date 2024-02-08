class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix = []
        arr = [int(i) for i in s]
        sum = 0
        count = 0
        for i in range(len(arr)):
            sum += int(s[i])
            prefix.append(sum)

        for i in range(len(s)):
            if s[i] == "1":
                if i > 0:
                    count += (i - prefix[i - 1] ) * ((len(s) - 1 - i) - (prefix[-1]  - prefix[i]))
            else:
                if i > 0:
                    count += (prefix[i - 1] * (prefix[-1]  - prefix[i]))

        return count
