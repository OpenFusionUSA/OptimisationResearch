# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]
        def dfs(node,i,j):
            if not node:
                return
            nodes.append((j,i+j,node.val))
            dfs(node.left, i+1, j-1)
            dfs(node.right, i+1, j+1)
        dfs(root, 0, 0)
        nodes.sort()
        resp=[]
        prev=-200000
        for j,i,value in nodes:
            if prev!=j:
                resp.append([])
                prev=j
            resp[-1].append(value)
        return resp