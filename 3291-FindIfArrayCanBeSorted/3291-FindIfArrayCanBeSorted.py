# Last updated: 7/22/2025, 3:23:40 PM
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def count_set_bits(num):

            count = 0
            while num:
                if num & 1:
                    count += 1
                num >>= 1
            return count

        arr = [(num, count_set_bits(num)) for num in nums]

        i, j = 0, 0
        is_swapped = False
        for i in range(len(nums)):
            is_swapped = False
            for j in range(1, len(nums)):
                if arr[j][0] < arr[j - 1][0] and arr[j][1] == arr[j - 1][1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    is_swapped = True

            if not is_swapped:
                break

        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False

        return True


        

