# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        q = deque([root])
        even = True
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if even:
                if any(v % 2 == 0 for v in vals) or any(vals[i] >= vals[i+1] for i in range(len(vals)-1)):
                    return False
            else:
                if any(v % 2 == 1 for v in vals) or any(vals[i] <= vals[i+1] for i in range(len(vals)-1)):
                    return False
            even = not even
        return True