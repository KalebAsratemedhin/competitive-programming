# Last updated: 7/22/2025, 3:24:47 PM
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        first = second = 0
        ans = []

        while first < len(nums1) and second < len(nums2):
            if nums1[first][0] == nums2[second][0]:
                ans.append([nums1[first][0], nums1[first][1] + nums2[second][1]])
                first += 1
                second += 1
            elif nums1[first][0] < nums2[second][0]:
                ans.append([nums1[first][0], nums1[first][1]])
                first += 1

            else:
                ans.append([nums2[second][0], nums2[second][1]])
                second += 1

                
        while first < len(nums1):
            ans.append([nums1[first][0], nums1[first][1]])
            first += 1
        
        while second < len(nums2):
            ans.append([nums2[second][0], nums2[second][1]])
            second += 1
        
        return ans
        