class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        left = {}
        right = {}
        n = len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
            
        sum = 0
        for i in range(len(arr)):
            pair = [-1,n]
            if i in left:
                pair[0] = left[i]
            if i in right:
                pair[1] = right[i]
            sum += ((pair[1] - i ) * (i - pair[0] )) * arr[i]
        return sum % (10**9 + 7)