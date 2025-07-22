# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        def dfs(node):
            if node is None:
                return 0
            dfs(node.left)
            cnt[node.val] += 1
            dfs(node.right)
        dfs(root)
        max_freq = max(cnt.values())
        ans = [val for val, freq in cnt.items() if freq == max_freq]
        return ans