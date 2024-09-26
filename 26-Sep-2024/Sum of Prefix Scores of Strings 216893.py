# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')

            if index not in curr.children:
                curr.children[index] = TrieNode()
            
            curr = curr.children[index]
            curr.count += 1
    
    def search(self, word):
        curr = self.root
        ans = 0

        for c in word:
            index = ord(c) - ord('a')
            
            if index not in curr.children:
                return ans
            
            ans += curr.children[index].count 
            curr = curr.children[index]

        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        ans = [0 for i in range(len(words))]
        trie = Trie()

        for word in words:
            trie.insert(word)

        for ind, word in enumerate(words):
            ans[ind] = trie.search(word)
            
        return ans
            
        