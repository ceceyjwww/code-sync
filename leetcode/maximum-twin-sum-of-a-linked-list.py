# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        ans = 0
        while head2:
            ans = max(ans, head2.val + head.val)
            head2 = head2.next
            head = head.next
        return ans