# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next and curr.next.next:
            val = curr.next.val
            if curr.next.next.val == val:
                while curr.next and curr.next.val == val:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next