# Last updated: 7/22/2025, 3:23:52 PM
class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        placeholder = seeker = n - 1 
        count = 0

        arr = [c for c in s]

        for seeker in range(n - 1, -1, -1):

            if arr[seeker] == '1' and arr[placeholder] == '0':
                count += placeholder - seeker
                arr[seeker], arr[placeholder] = arr[placeholder], arr[seeker] 
                placeholder -= 1
            elif arr[placeholder] == '1':
                placeholder -= 1

        return count
                