class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        left  = 0
        right = n - 1
        ans = skill[left] + skill[right]
        chemistries = 0
        while left < right:
            if skill[left] + skill[right] == ans:
                chemistries += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return chemistries
        