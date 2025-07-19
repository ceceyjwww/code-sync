# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = self.reverseList(head)
        curr = head2
        while curr.next:
            
            if curr.next.val < curr.val:
                curr.next = curr.next.next
            else:
                
                curr = curr.next
        return self.reverseList(head2)