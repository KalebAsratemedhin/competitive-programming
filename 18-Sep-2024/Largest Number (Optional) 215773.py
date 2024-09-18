# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                

                a = arr[i] + arr[j]
                b = arr[j] + arr[i]

                for k in range(len(a)):
                    if a[k] > b[k]:
                        break
                    if a[k] < b[k]:
                        arr[i], arr[j] = arr[j], arr[i]

                        break

        for i in range(len(arr) - 1):
            if arr[i] != '0':
                break
            arr[i] = ''
                        
        return "".join(arr)


                



