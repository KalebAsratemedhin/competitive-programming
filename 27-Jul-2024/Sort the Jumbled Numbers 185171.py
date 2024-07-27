# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            number = []
            for d in str(num):
                mapped = mapping[int(d)]
                if not mapped and not number:
                    continue
                number.append(str(mapped))
            if not number:
                number = 0
            else:
                number = int("".join(number))
            arr.append((number, i))
            
        arr.sort()
        for i, (mapped, j) in enumerate(arr):
            arr[i] = nums[j]
        return arr