class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        kinds = Counter(answers)
        count = 0
        for key, val in kinds.items():
            if key == 0:
                count += val
            elif val > key + 1:
                groups = val // (key + 1) + (1 if val % (key + 1) else 0)
                count += groups * (key + 1)
            else:
                count += 1 + key
        return count