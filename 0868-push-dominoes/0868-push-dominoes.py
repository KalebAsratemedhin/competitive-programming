class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = []
        rights = 0
        dots = 0

        for domino in range(len(dominoes)):
            if dominoes[domino] == '.':
                dots += 1
            elif dominoes[domino] == 'R':
                for i in range(dots):
                    if rights == 1:
                        ans.append('R')
                    else:
                        ans.append('.')
                ans.append('R')
                dots = 0
                rights = 1
              
            else:
                if rights == 1:
                    half = dots // 2
                    for i in range(half):
                        ans.append('R')
                    if dots % 2 == 1:
                        ans.append('.')
                    for i in range(half):
                        ans.append('L')
                    ans.append('L')
                    rights = 0
                    
                    
                else:
                    for j in range(dots):
                        ans.append('L')
                    ans.append('L')
                dots = 0

        for i in range(dots):
            if rights == 1:
                ans.append('R')
            else:
                ans.append('.')
        return "".join(ans)
                    
                    
