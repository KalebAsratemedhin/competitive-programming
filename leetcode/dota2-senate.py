class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while dire and radiant:
            if dire[0] < radiant[0]:
                dire.append(dire[0] + len(senate))
            else:
                radiant.append(radiant[0] + len(senate))

            radiant.popleft()
            dire.popleft()

        if dire:
            return "Dire"
        return "Radiant"
