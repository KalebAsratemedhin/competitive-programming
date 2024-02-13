# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        

        while fast and fast.next and fast.next.next:
            # the odd  to be moved
            pos = fast.next.next

            # write before the odd
            fast = fast.next

            # the next even
            temp = slow.next

            slow.next = pos

            # remove the odd
            fast.next = pos.next

            # continue with the evens
            pos.next = temp
            
            # prepare place for the next odd
            slow = slow.next
            


            
        return head

1