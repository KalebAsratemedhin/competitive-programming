# Last updated: 7/22/2025, 3:23:55 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for i, word in enumerate(words):
            if x in set(word):
                ans.append(i)
        return ans