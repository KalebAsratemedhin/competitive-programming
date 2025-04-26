class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = start = count = 0
        window = defaultdict(int)

        # 1,3,5,1,2,5,5
        #  1 1 1 1

        if minK >  maxK:
            return 0
        near_min = near_max = near_pair = -1
        
        for index, num in enumerate(nums):
            if num == minK:
                if minK == maxK:
                    near_max = index
                if near_max != -1:
                    count += near_max - start + 1
                    near_pair = near_max   
                near_min = index
            elif num == maxK:
                if near_min != -1:
                    count += near_min - start + 1
                    near_pair = near_min   

                near_max = index
            elif minK <= num <= maxK:
                if near_pair != -1:
                    count += near_pair - start + 1
            else:
                start = index + 1
                near_min = near_max = near_pair = -1

        return count


