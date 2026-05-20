# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)
    def isSubtree(self,root:Optional[TreeNode],subroot:Optional[TreeNode]) -> bool:
        if subroot is None:
            return True
        if root is None:
            return False
        if self.sameTree(root,subroot):
            return True
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
