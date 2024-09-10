# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

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

        