# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0:
            if n >= 0:
                if nums1[m] > nums2[n]:
                    nums1[j] = nums1[m]
                    j -= 1
                    m -= 1
                else:
                    nums1[j] = nums2[n]
                    n -= 1
                    j -= 1
            else:
                break
        while n >= 0:
            nums1[j] = nums2[n]
            n -= 1
            j -= 1