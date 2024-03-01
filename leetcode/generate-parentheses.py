class Solution:
    def generateParenthesis(self, n):
        def generate(arr, opened, closed, result):
            if len(arr) == 2 * n:
                result.append("".join(arr))
                return

            if opened < n:
                arr.append("(")
                generate(arr, opened + 1, closed, result)
                arr.pop()

            if closed < opened:
                arr.append(")")
                generate(arr, opened, closed + 1, result)
                arr.pop()  

        result = []
        generate([], 0, 0, result)
        return result
        