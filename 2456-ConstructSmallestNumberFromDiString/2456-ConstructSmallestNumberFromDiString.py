# Last updated: 7/22/2025, 3:25:57 PM
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = [i for i in range(1, len(pattern) + 2)]

        for i in range(len(pattern)):
            for index, letter in enumerate(pattern):
                if letter == 'I' and ans[index] > ans[index + 1]:
                    ans[index], ans[index + 1] = ans[index + 1], ans[index]
                if letter == 'D' and ans[index] < ans[index + 1]:
                    ans[index], ans[index + 1] = ans[index + 1], ans[index]


        return "".join(list(map(str, ans)))


