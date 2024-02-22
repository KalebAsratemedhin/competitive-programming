# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        per_part = n // k
        rem = n % k
        if not per_part:
            per_part = 1
            rem = 0
        curr = head
        ans = []
        i = 0
        while curr :
            prev = curr
            ans.append(curr)
            for j in range(i, i + per_part):
                if curr:
                    prev = curr
                    curr = curr.next

            i += per_part
            if rem > 0:
                rem -= 1
                i += 1
                temp = curr.next
                curr.next = None
                curr = temp

            else:
                prev.next = None

        while len(ans) < k:
            ans.append(None)
            
        return ans
