# Last updated: 7/22/2025, 3:24:03 PM
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        time = 0
        n = len(tasks)
        
        for i in range(n):
            if i % 4 == 0:
               time = max(time, processorTime[i // 4] + tasks[i])

        return time