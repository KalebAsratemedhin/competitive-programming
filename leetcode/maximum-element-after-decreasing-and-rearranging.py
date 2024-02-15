class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        map = {}
        greater = 0
        surplus = 0
        n = len(arr)
        maximum = n

        for i in range(n):
            map[arr[i]] = map.get(arr[i], 0) + 1
            if arr[i] > n:
                greater += 1
            
        for i in range(n, 0, -1):
            if i not in map: 
                if greater > 0:
                    greater -= 1
                elif surplus > 0:
                    surplus -= 1
                else:
                    maximum -= 1
            elif i in map and map[i] > 1:
                surplus += map[i] - 1
        return maximum


            


