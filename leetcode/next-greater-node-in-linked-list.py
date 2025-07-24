# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
            n += 1

        print(vals)
        ans = [0] * n
        st = []
        for i, x in enumerate(vals):
            while st and x > vals[st[-1]]:
                ans[st[-1]] = x
                st.pop()
            st.append(i)
        return ans