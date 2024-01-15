class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            start = i
            end = (start + nums[i]) % n
            if start == end:
                continue
            count = 0
            while count <= n:
                if nums[end] * nums[start] < 0:
                    break
                prev = end
                end = (end + nums[end]) % n
                if end == prev:
                    break
                if end == start:
                    return True
                count += 1
            
        return False