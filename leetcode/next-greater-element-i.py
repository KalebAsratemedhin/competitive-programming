class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dict = defaultdict(lambda: -1)
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dict[stack.pop()] = nums2[i]
            
            stack.append(nums2[i])
        
        for n in nums1:
            ans.append(dict[n])
            
        return ans
                
                    