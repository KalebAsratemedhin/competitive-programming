class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flips = []
        for j in range(n):
            max_index = 0
            for i in range(n - j):
                if arr[i] > arr[max_index]:
                    max_index = i
            l = 0
            r = max_index
            if l != r:
                flips.append(max_index + 1)
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            l = 0
            r = n - 1 - j
            flips.append(r + 1)
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        return flips
            
        
            
            

