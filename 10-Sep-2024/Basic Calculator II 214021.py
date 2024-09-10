# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        3 * 4 + 2 * 9
        nums = []
        ops = []
        operations = {'*', '/', '+', '-'}
        i = 0

        while i < len(s):

            if s[i] in operations:
                ops.append(s[i])
                i += 1

            num = []

            while i < len(s) and s[i] not in operations:
                if s[i]:
                    num.append(s[i])
                i += 1
            num = int("".join(num))
            nums.append(num)

            if ops and ops[-1] == "*":
                x, y = nums.pop(), nums.pop()
                ops.pop()
                nums.append(x * y)
            elif ops and ops[-1] == "/":
                y, x = nums.pop(), nums.pop()
                ans = floor(x / y)
                ops.pop()
                nums.append(ans)

        curr = nums[0]
        i = 1

        for op in ops:
            if op == '+':
                curr = nums[i] + curr
            elif op == '-':
                curr = curr - nums[i]
            i += 1
        return curr

 

            