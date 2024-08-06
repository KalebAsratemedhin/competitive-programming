# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        uniques = list(freq.items())
        uniques.sort(key = lambda x: x[1], reverse=True)
        cost = 1
        count = ans = 0

        for c, val in uniques:
            count += 1
            ans += cost * val

            if count == 8:
                cost += 1
                count = 0


        return ans