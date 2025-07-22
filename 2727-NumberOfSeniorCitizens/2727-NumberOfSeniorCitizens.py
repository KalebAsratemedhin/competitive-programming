# Last updated: 7/22/2025, 3:24:38 PM
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        for i in range(len(details)):
            male = details[i].split('M')
            female = details[i].split('F')
            odd = details[i].split('O')

            if len(male) == 2:
                details[i] = int(male[1][:2])
            elif len(female) == 2:
                details[i] = int(female[1][:2])
            else:
                details[i] = int(odd[1][:2])

        details.sort()
        for i in range(len(details)):
            if details[i] > 60:
                return len(details) - i

        return 0