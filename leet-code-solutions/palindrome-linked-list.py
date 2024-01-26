# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseCopy(self, head):
        prev = ListNode(head.val)
        if head.next == None:
            return prev
        curr = head.next
        counter = curr
        while counter.next != None:
            curr = ListNode(counter.val)
            curr.next = prev
            prev = curr
            curr = curr.next
            counter = counter.next
        curr = ListNode(counter.val)
        curr.next = prev
        return curr
    def isPalindrome(self, head):
        index1 = head
        index2 = self.reverseCopy(head)
        while index1 !=None  and index2 != None:
            if index1.val != index2.val:
                return False
            index1 = index1.next
            index2 = index2.next
        return True  