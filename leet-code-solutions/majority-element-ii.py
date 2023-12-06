class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = Counter(nums)
        cutoff = n // 3
        elements = []
        keys = hashmap.keys()
        for k in keys:
            if hashmap[k] > cutoff:
                elements.append(k)
        return elements