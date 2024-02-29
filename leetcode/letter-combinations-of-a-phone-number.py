class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        combo = []
        dict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        def helper(start):
            if start >= len(digits):
                if combo:
                    ans.append("".join(combo))
                return
            
            for i in dict[int(digits[start])]:
                combo.append(i)
                helper(start + 1)
                combo.pop()
        helper(0)
        return ans



