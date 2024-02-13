# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        curr = headA

        while curr:
            lenA += 1
            curr = curr.next
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next

        currA = headA
        currB = headB
        diff = abs(lenA - lenB)
        
        if lenA > lenB:
            while diff > 0:
                currA = currA.next
                diff -= 1

        elif lenB > lenA:
            while diff > 0:
                currB = currB.next
                diff -= 1

        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next

        return None
        