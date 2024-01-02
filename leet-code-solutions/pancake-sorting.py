class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flips = []
        for j in range(n, 1, -1):
            max_index = arr.index(j)
            if max_index == j - 1:
                continue
            
            if max_index != 0:
                r = max_index
                l = 0
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
                flips.append(max_index + 1)
            r = j - 1
            l = 0
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            flips.append(j)
           
        return flips
            
        
            
            

