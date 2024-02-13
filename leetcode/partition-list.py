# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        holder = dummy
        seeker = head
        prev = dummy

        while seeker:
            if seeker.val < x:
                if seeker == holder.next:
                    holder = holder.next
                    seeker = seeker.next
                else:
                    prev.next = seeker.next
                    seeker.next = holder.next
                    holder.next = seeker
                    holder = holder.next
                    seeker = prev.next
            else:
                prev = seeker
                seeker = seeker.next

        return dummy.next




            
