# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        fast = dummy
        slow = dummy
        dummy.next = head

        while fast.next:
            if n > 0:
                fast = fast.next
                n -= 1
            else:
                fast = fast.next
                slow = slow.next

        slow.next = slow.next.next

        return dummy.next
        