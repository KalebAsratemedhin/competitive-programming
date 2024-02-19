class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = deque(sorted(deck, reverse = True))
        ans = deque()
        n = len(deck)

        while n > len(ans):
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(deck.popleft())
        return ans
        