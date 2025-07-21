# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_abs = inf
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = None
        def f(root):
            if root is None:
                return
            nonlocal pre
            f(root.left)
            if pre is not None:
                self.min_abs = min(self.min_abs, abs(root.val - pre))
            pre = root.val
            f(root.right)
        f(root)
        return self.min_abs