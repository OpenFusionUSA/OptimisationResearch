# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]
        def dfs(root,i,j):
            if not root:
                return
            nodes.append((j,i,root.val))
            dfs(root.left,i+1,j-1)
            dfs(root.right,i+1,j+1)
        dfs(root, 0, 0)
        nodes.sort()
        ans=[]
        prev=-2000
        for j,_,value in nodes:
            if prev!=j:
                ans.append([])
                prev=j
            ans[-1].append(value)
        return ans

        