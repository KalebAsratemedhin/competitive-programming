class Solution:
    def minimumSteps(self, s: str) -> int:
        holder = 0
        seeker = 1
        steps = 0
        arr = list(s)
        
        while seeker < len(s):
            if arr[seeker] == "0" and arr[holder] == "1":
                steps += (seeker - holder)
                arr[seeker], arr[holder] = arr[holder], arr[seeker]
                holder += 1
            elif arr[holder] == "0":
                holder += 1
            
            seeker += 1
        return steps
            


