class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentenceArr = sentence.split()
        n = len(sentenceArr)
        m = len(searchWord)

        for i in range(n):
            matches = 0
            if len(sentenceArr[i]) < m:
                continue
            for j in range(m):
                if sentenceArr[i][j] != searchWord[j]:
                    break
                matches += 1
            if matches == m:
                return i + 1
        return -1
            




