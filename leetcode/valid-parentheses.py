class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {"(":")","[":"]","{":"}"}
        for i in s:
            if i in opens:
                stack.append(i)
            elif stack:
                if opens[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            elif not stack:
                return False
        if stack:
            return False
        return True
        

