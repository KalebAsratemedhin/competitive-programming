# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(prev, node1, node2):
            if not node1 and not node2:
                return 
            if not node1:
                prev.next = node2
                prev = node2
                merge(prev, node1, node2.next)
                return
            if not node2:
                prev.next = node1
                prev = node1
                merge(prev, node1.next, node2)
                return

            if node1.val < node2.val:
                prev.next = node1
                prev = node1
                merge(prev, node1.next, node2)
            else:
                prev.next = node2
                prev = node2
                merge(prev, node1, node2.next)
            return
        
        head = ListNode()
        merge(head, list1, list2)
        return head.next