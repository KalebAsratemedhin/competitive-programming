# Last updated: 7/22/2025, 3:27:02 PM
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        time = 0
        for i in range(len(tickets)):
            queue.append([tickets[i], i])
        while queue and (queue[0][1] != k or queue[0][0] != 1):
            served = queue.popleft()
            served[0] -= 1
            time += 1
            if served[0] > 0:
                queue.append(served)
        return time + 1