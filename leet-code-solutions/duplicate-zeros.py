class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        stack = []
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                stack.append(arr[i])
            stack.append(arr[i])
            arr[i] = stack.pop(0)
