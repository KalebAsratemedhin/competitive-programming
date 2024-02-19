class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        arr = 2 * nums
        ans = [-1] * len(arr) 
        for i in range(len(arr)):
            if stack:
                while stack and arr[stack[-1]] < arr[i]:
                    ans[stack.pop()] = arr[i]
                stack.append(i)
            else:
                stack.append(i)

        return ans[:len(nums)]

        