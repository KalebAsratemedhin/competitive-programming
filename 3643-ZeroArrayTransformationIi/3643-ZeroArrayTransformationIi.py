# Last updated: 7/22/2025, 3:22:54 PM
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        '''
        O(n * log n)


        1. find candidates of k as low + high // 2
        2. for the first k queries, add val to left pointer and subtract from right + 1 ppointer
        3. do prefix sum and check if num is greater than prefix at that index return false
        4. else return true
        5. if true, go(bisect) left
        6. if false, go(bisect) right
        7. return low
        

        '''

        def is_enough(k):
            prefix = [0] * (len(nums) + 1)

            for i in range(k):
                left, right, val = queries[i]
                prefix[left] += val
                prefix[right + 1] -= val

            
            for i in range(1, len(nums)):
                prefix[i] += prefix[i - 1]

            for i in range(len(nums)):
                if nums[i] > prefix[i]:
                    return False

            return True            
            

        n = len(queries)
        low, high = 0, n

        while low <= high:
            mid = (low + high) // 2
            if is_enough(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return -1 if low > n else low 

