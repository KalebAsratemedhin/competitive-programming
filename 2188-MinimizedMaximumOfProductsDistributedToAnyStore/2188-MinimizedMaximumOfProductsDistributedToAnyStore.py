# Last updated: 7/22/2025, 3:27:03 PM
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low = 1
        high = 10 ** 5

        def partitions(k):
            total = 0

            for q in quantities:
                div, rem = divmod(q, k)
                total += div 
                if rem:
                    total += 1
            
            return total

        
        while low < high:
            mid = (low + high) // 2

            if partitions(mid) > n:
                low = mid + 1
            else:
                high = mid
        
        return high









