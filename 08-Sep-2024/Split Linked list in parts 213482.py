# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0

        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        div, rem = divmod(n, k)

        curr = head
        ans = []

        while curr:
            m = div + 1 if rem else div 
            if m >= 1:
                if rem:
                    rem -= 1
                ans.append(curr)
                for i in range(m - 1):
                    curr = curr.next
                temp = curr.next
                curr.next = None
                curr = temp
        
        l = k - len(ans)

        while l > 0:
            ans.append(None)
            l -= 1

        return ans
            
