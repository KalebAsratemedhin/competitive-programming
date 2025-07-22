# Last updated: 7/22/2025, 3:26:33 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = ListNode()
        dummy = prev

        while curr:
            sum = 0
            while curr.val:
                sum += curr.val
                temp = curr.next
                curr.next = None
                curr = temp
                
            prev.next = ListNode(sum, curr.next)
            prev = prev.next
            curr = prev.next
        return dummy.next
