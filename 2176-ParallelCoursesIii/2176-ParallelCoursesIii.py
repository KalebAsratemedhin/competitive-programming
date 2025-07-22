# Last updated: 7/22/2025, 3:27:09 PM
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjacents = [[] for i in range(n)]
        indegrees =  [0] * n
        duration = [0] * n
        total_time = 0

        for u, v in relations:
            adjacents[u - 1].append(v - 1)
            indegrees[v - 1] += 1
        
        queue = deque()
        for i in range(n):
            if not indegrees[i]:
                queue.append(i)
                duration[i] += time[i]
                total_time = max(total_time, duration[i])
        
        while queue:
            node = queue.popleft()
            for adj in adjacents[node]:
                indegrees[adj] -= 1
                duration[adj] = max(duration[node] + time[adj], duration[adj])
                total_time = max(duration[adj], total_time)
                
                if not indegrees[adj]:
                    queue.append(adj)

        return total_time




        