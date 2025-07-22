# Last updated: 7/22/2025, 3:23:41 PM
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