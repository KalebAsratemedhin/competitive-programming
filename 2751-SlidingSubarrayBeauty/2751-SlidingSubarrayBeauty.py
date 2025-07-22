# Last updated: 7/22/2025, 3:24:37 PM
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        dic = {i: 0 for i in range(-50, 51, 1)}
        ans = []
        left = 0

        for right in range(len(nums)):
            if right - left >= k:
                dic[nums[left]] -= 1
                left += 1

            if right - left < k:
                dic[nums[right]] += 1
                if right - left == k - 1:
                    y = x
                    for i in range(-50, 0, 1):
                        if dic[i]:
                            y -= dic[i]
                        if y <= 0:
                            ans.append(i)
                            break

                    else:
                        ans.append(0)

        return ans

            
            



