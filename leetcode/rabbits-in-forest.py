class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = {}
        total = 0
        for i in range(len(answers)):
            rabbits[answers[i]] = rabbits.get(answers[i], 0) + 1
        for key, value in rabbits.items():
            
            total += (key + 1) * (value // (key + 1))
            if value % (key + 1) != 0:
                total += key + 1
        return total
                


