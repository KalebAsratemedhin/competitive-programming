# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        pointers = [0 for i in range(n)]
        
        heap = [[nums2[pointers[i]] + nums1[i], i] for i in range(n)]
        heapq.heapify(heap)

        ans = []

        while heap and len(ans) < k:
            sum, ind = heapq.heappop(heap)
            ans.append([nums1[ind], nums2[pointers[ind]]])
            pointers[ind] += 1
            
            if pointers[ind] < m:
                heapq.heappush(heap, [nums2[pointers[ind]] + nums1[ind], ind])

        return ans
