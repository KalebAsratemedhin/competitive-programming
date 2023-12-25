class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peaked = False
        if len(arr) < 3:
            return False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if i < len(arr) - 1 and arr[i] < arr[i + 1] and arr[i] < arr[i - 1]:
                return False
            if peaked and arr[i] >= arr[i - 1]:
                return False
            elif not peaked and arr[i] > arr[i - 1]:
                if i < len(arr) - 1 and arr[i + 1] < arr[i]:
                    peaked = True

        return peaked

            
