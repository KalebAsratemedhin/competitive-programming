# Last updated: 7/22/2025, 3:24:22 PM
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        arr = [[i + 1, pos, directions[i], healths[i]] for i, pos in enumerate(positions)]
        arr.sort(key= lambda x: x[1])
        stack = []
        for i, pos, direction, health in arr:
            curr_health = health
            while stack and stack[-1][2] == 'R' and direction == 'L':
                if curr_health < stack[-1][3]:
                    stack[-1][3] -= 1
                    curr_health = 0
                    break
                elif curr_health > stack[-1][3]:
                    stack.pop()
                    curr_health -= 1
                    
                else:
                    stack.pop()
                    curr_health = 0
                    break
            if curr_health:
                stack.append([i, pos, direction, curr_health])

        stack.sort(key= lambda x: x[0])
        return [s[3] for s in stack]



