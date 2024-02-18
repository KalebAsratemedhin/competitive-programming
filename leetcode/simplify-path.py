class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split("/")
        for i in arr:
            if stack and i =="..":
                stack.pop()
            elif i and i != "." and i != "..":
                stack.append(i)
        return  "/" + "/".join(stack)

