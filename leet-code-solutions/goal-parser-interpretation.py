class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                ans += 'G'
                i += 1
            elif command[i] == '(':
                if i + 1 < n:
                    if command[i + 1] == ')':
                        ans += 'o'
                        i += 2
                    elif command[i + 1] == 'a':
                        ans += "al"
                        i += 4
                else:
                    break
        return ans
            
            