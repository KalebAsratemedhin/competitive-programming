# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = {}
        ans = []
        for c in "qwertyuiop":
            row[c] = 1
        for c in "asdfghjkl":
            row[c] = 2
        for c in "zxcvbnm":
            row[c] = 3
        
        for word in words:
            r = row[word[0].lower()]
            one_row = True
            
            for char in word:
                if row[char.lower()] != r:
                    one_row = False
                    break

            if one_row:
                ans.append(word)

        return ans
            
                
        
