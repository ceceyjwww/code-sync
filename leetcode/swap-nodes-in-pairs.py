# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        dummy = ListNode(next = head)
        p0 = dummy

        prev = None
        curr = p0.next

        while n >= 2:
            n -= 2
            for _ in range(2):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            nxt = p0.next
            p0.next.next = curr
            p0.next = prev
            p0 = nxt
        
        return dummy.next