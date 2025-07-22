# Last updated: 7/22/2025, 3:24:25 PM
class Solution:
    def minimumCost(self, s: str) -> int:
            n = len(s)
            
            forward_cost = [0] * n
            backward_cost = [0] * n
            
            for i in range(1, n):
                if s[i] == s[i - 1]:
                    forward_cost[i] = forward_cost[i - 1]     
                else:
                    forward_cost[i] = forward_cost[i - 1] + i 
            
            for i in range(n - 2, -1, -1):
                if s[i] == s[i + 1]:
                    backward_cost[i] = backward_cost[i + 1]     
                else:
                    backward_cost[i] = backward_cost[i + 1] + n - 1 - i    
                    
            min_cost = backward_cost[0]
            
            for i in range(n):
                total_cost = forward_cost[i] + backward_cost[i]
                if total_cost < min_cost:
                    min_cost = total_cost
                    
            return min_cost
