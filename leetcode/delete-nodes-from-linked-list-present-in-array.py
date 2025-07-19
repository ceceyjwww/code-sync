# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        st = set(nums)
        while curr.next:
            val = curr.next.val
            if val in st:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next