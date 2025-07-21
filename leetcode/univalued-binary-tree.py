# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        def f(node, val):
            if node is None:
                return True
            if node.val != val:
                return False
            return f(node.left, val) and f(node.right, val)
        return f(root, val)