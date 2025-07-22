# Last updated: 7/22/2025, 3:24:15 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = head
        curr = head.next

        while curr:
            value = gcd(prev.val, curr.val)
            new_node = ListNode(val=value)
            prev.next = new_node
            new_node.next = curr
            prev = curr
            curr = curr.next


        return head

        