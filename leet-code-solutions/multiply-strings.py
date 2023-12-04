class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = 0
        m = 0
        for i in range(len(num1) - 1, -1, -1):
            n += (10 ** i )* int(num1[len(num1) - 1 - i])
        for j in range(len(num2) - 1, -1, -1):
            m += (10 ** j ) * int(num2[len(num2) - 1 - j])
        return str(n * m)

