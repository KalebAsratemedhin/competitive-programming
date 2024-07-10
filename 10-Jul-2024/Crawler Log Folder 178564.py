# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for l in logs:
            d = l[:-1]
            if d == ".." and stack:
                stack.pop()
            elif d != "." and d != "..":
                stack.append(d)
        return len(stack)