# Last updated: 7/22/2025, 3:26:06 PM
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank_dict = Counter(ranks)
        suits_dict = Counter(suits)
        ans = 0

        if len(suits_dict) == 1:
            return "Flush"
        for key, value in rank_dict.items():
            if value >= 3:
                ans = 3
            elif value >= 2 and ans != 3:
                ans = 2
        if ans == 2:
            return "Pair"
        elif ans == 3:
            return "Three of a Kind"

        return "High Card"