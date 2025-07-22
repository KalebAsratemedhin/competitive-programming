# Last updated: 7/22/2025, 3:25:36 PM
class Solution:
    def __init__(self):
        self.count = 0

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        def merge(arr, start, mid, end):
            left = arr[start : mid + 1]
            right = arr[mid + 1: end + 1]
            l, r = 0, 0
            ind = start
            

            while l < len(left) and r < len(right):
                if left[l] <= right[r] + diff:
                    self.count += len(left) - l
                    r += 1
                else:
                    l += 1
            
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] >= right[r]:
                    arr[ind] = left[l]
                    ind += 1
                    l += 1
                else:
                    arr[ind] = right[r]
                    ind += 1
                    r += 1

            
            while l < len(left):
                arr[ind] = left[l]
                ind += 1
                l += 1
            
            while r < len(right):
                arr[ind] = right[r]
                ind += 1
                r += 1

        def mergeSort(arr, start, end):
            if start == end:
                return 

            mid = (start + end) // 2

            mergeSort(arr, start, mid)
            mergeSort(arr, mid + 1, end)
            merge(arr, start, mid, end)
            
        mergeSort(arr, 0, len(arr) - 1)
        return self.count