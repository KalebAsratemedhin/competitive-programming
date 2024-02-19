class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        dict = {}

        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if len(stack) + 1 in dict:
                    dict[len(stack)] = dict.get(len(stack), 0) + (2 * dict[len(stack) + 1])
                    del dict[len(stack) + 1]
                else:
                    dict[len(stack)] = dict.get(len(stack), 0) + 1
                stack.pop()
        score = dict[1]   
        return score