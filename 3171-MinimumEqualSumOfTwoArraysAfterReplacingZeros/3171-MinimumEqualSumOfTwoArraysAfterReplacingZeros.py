# Last updated: 7/22/2025, 3:24:00 PM
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        z1, z2 = nums1.count(0), nums2.count(0)
        sum1, sum2 = sum(nums1), sum(nums2)

        if sum2 == sum1: 
            if z1 and z2 or not z1 and not z2:
                return sum1 + max(z1, z2)
            return -1

        elif sum1 > sum2:
            if z2 and not z1:
                if sum1 - sum2 < z2:
                    return -1
                return sum1
            elif z2 and z1:
                if z1 > z2:
                    return sum1 + z1
                return sum2 + max(sum1 - sum2 + z1, z2)
            return -1
        elif sum2 > sum1:
            if z1 and not z2:
                if sum2 - sum1 < z1:
                    return -1
                return sum2
            elif z1 and z2:
                if z2 > z1:
                    return sum2 + z2
                return sum1 + max(sum2 - sum1 + z2, z1)
        return -1



