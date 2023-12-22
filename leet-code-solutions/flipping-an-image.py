class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            r = n - 1
            l = 0
            while l <= r:
                if row[l] == row[r]:
                    row[l] = int(not(row[r]))
                    row[r] = row[l]
                r -= 1
                l += 1
        return image
