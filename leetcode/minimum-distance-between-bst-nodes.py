# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        pre = None
        min_abs = inf
        def f(node):
            if node is None:
                return
            nonlocal pre, min_abs
            f(node.left)
            if pre is not None:
                min_abs = min(min_abs, abs(node.val - pre))
            pre = node.val
            f(node.right)
        f(root)
        return min_abs