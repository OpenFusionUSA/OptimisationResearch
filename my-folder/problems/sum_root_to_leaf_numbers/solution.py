# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s=0
        stack=[(root,0)]
        while stack:
            root,cur_num=stack.pop()
            if root is not None:
                cur_number=cur_num*10+root.val
                if root.left is None and root.right is None:
                    s+=cur_number
                else:
                    stack.append((root.left,cur_number))
                    stack.append((root.right,cur_number))
        return s