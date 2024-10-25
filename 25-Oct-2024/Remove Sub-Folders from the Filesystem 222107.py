# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        '''

        "/a","/a/b","/c/d","/c/d/e","/c/f"



        '''

        ans = []
        folder.sort()

        left = 0
        n = len(folder)

        while left < n:
            ans.append(folder[left])
            right = left + 1
            while right < n and folder[left] + '/' == folder[right][:len(folder[left]) + 1]:
                right += 1
            left = right
        
        return ans
            
