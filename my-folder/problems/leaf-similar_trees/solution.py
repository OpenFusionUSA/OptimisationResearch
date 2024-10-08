# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root:
                if not root.left and not root.right:
                    yield root.val
                yield from dfs(root.left)
                yield from dfs(root.right)
        return list(dfs(root1))==list(dfs(root2))