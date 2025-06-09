class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        curr = []
        ans = []

        def dfs():
            if int("".join(curr)) > n:
                return 
            ans.append(int("".join(curr)))

            for digit in range(0, 10):
                curr.append(str(digit))
                dfs()
                curr.pop()

        for digit in range(1, 10):
            curr = [str(digit)]
            dfs()

        return ans

