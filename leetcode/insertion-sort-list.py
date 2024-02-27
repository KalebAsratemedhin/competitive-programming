# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"))
        curr = head

        while curr:
            temp = curr.next
            sortd = dummy
            prev = sortd

            while sortd and  curr.val > sortd.val:
                prev = sortd
                sortd = sortd.next

            prev.next = curr
            curr.next = sortd
            curr = temp

        return dummy.next