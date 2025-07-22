# Last updated: 7/22/2025, 3:23:57 PM
class Solution:
    def minChanges(self, s: str) -> int:
        '''

        '''

        # count of changes
        count = 0

        # iterate by two
        for i in range(0, len(s), 2):
            # if pairs don't match add 1 to count
            if s[i] != s[i + 1]:
                count += 1
        
        # return count
        return count

