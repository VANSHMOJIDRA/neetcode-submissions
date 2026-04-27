# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode') -> 'TreeNode':
        lcs = [root]

        def search(root):
            if not root:
                return
            lcs[0] = root
            if root is p and q is root:
                return root
            if p.val < root.val and q.val < root.val:
                return search(root.left)
            elif p.val > root.val and q.val > root.val:
                return search(root.right)
            else:
                return 
        search(root)
        return lcs[0]