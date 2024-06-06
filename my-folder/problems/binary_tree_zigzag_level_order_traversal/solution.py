# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=[]
        reverse=False
        q.append(root)
        while q:
            tempres=[]
            n=len(q)
            for _ in range(n):
                node=q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                tempres.append(node.val)
            if reverse:
                res.append(tempres[::-1])
                reverse=False
            else:
                res.append(tempres)
                reverse=True
        return res