class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "/", "*"}
        for t in tokens:
            if t in ops and len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                ans = eval(num1 + t + num2)
                if ans < 0:
                    stack.append(str(ceil(ans)))
                else:
                    stack.append(str(floor(ans)))
            else:
                stack.append(t)
        return int(stack[-1])
                