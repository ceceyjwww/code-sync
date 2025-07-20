# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = curr_max = 0
        def dfs(root: TreeNode, curr_max: int) -> None:
            if root is None:
                return
            nonlocal ans
            print(f"Visiting {root.val}, curr_max: {curr_max}")
            if root.val >= curr_max:
                ans += 1
            curr_max = max(root.val, curr_max)
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)
        dfs(root, root.val)
        return ans