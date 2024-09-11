# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
        
    def search(self, word: str):
        curr = self.root

        for i, c in enumerate(word):
            index = ord(c) - ord("a")

            if  curr.is_end:
                return word[ :i ]
            
            if not curr.children[index]:
                return ""
            curr = curr.children[index]
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        words = sentence.split()
        ans = []

        for word in dictionary:
            trie.insert(word)
        
        for word in words:
            root = trie.search(word)

            if root:
                ans.append(root)
            else:
                ans.append(word)
        
        return " ".join(ans)

        
