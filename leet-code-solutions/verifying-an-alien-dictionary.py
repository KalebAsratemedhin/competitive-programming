class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        for i, letter in enumerate(order):
            alphabet[letter] = i
        n = len(words)
        for i in range(n - 1):
            l = min(len(words[i]), len(words[i + 1]))
            ordered = True
            for j in range(l):
                if alphabet[words[i][j]] < alphabet[words[i + 1][j]]:
                    ordered = True
                    break
                elif alphabet[words[i][j]] > alphabet[words[i + 1][j]]:
                    return False
                else:
                    ordered = False           
            if not ordered and len(words[i]) > len(words[i + 1]):
                return False
        return True


