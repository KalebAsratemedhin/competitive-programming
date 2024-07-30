# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        for i in range(len(arr) - 1, -1, -1):
            max_num = None
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    if not max_num or (max_num and arr[j] > arr[max_num]):
                        max_num = j
            if max_num:
                arr[i], arr[max_num] = arr[max_num], arr[i]
                return arr
            
        return arr
                
