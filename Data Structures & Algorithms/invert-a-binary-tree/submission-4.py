# defination for tree node
# class TreeNode:
# def __init__(self,val = 0,left = none,right= none)
# self.val = val
# self.left = left
# self.right = right

class Solution:
    def invertTree(self,root:Optional(ListNode)) -> Optional(ListNode):
        if not root:
            return None
        
        root.left,root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root