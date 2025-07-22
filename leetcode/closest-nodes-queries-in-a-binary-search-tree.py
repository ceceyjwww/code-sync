# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        bst = []
        ans = []
        
        def f(node):
            nonlocal bst
            if node is None:
                return
            f(node.left)
            bst.append(node.val)
            f(node.right)
        f(root)
        print(bst)
        n = len(bst)
        
        for val in queries:
            i = bisect_left(bst, val)
            lower = bst[i-1] if i != 0 else -1
            upper = bst[i] if i < n else -1
            if i < n and bst[i] == val:
                lower = upper = val
            ans.append([lower, upper])
            
        return ans