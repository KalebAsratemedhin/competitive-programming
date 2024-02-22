# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        curr = head
        prev = dummy

        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        start = prev
        while right > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1

        if start and start.next:
            start.next.next = curr
            start.next = prev
        
        return dummy.next