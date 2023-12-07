class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_index = set(spaces)
        spaced_phrase = ""
        for i in range(len(s)):
            if i in space_index:
                spaced_phrase += " " 
            spaced_phrase += s[i]
        return spaced_phrase
