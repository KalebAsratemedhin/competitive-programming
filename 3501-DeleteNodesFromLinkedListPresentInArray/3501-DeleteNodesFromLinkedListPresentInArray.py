# Last updated: 7/22/2025, 3:23:11 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = dummy.next
        forbidden = set(nums)

        while curr:
            if curr.val not in forbidden:
                prev.next = curr
                prev = curr
                curr = curr.next
            else:
                curr = curr.next

        prev.next = None
        return dummy.next
                