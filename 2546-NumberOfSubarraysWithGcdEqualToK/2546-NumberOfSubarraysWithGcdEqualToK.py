# Last updated: 7/22/2025, 3:25:30 PM
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcf(num1, num2):
            if num2 == 0:
                return num1

            return gcf(num2, num1 % num2)

        count = 0


        for i in range(len(nums)):
            gcfs = [nums[i]]
            for j in range(i, len(nums)):
                
                gcfs.append(gcf(gcfs[-1], nums[j]))
                if gcfs[-1] == k:
                    count += 1

        return count


