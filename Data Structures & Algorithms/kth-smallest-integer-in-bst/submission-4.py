# CLASS TREENODE:
# DEF __INIT__ (SELF,VAL=0,LEFT=NONE,RIGHT=NONE):
# SELF.VAL = VAL
# SELF.LEFT = LEFT
# SELF.RIGHT = RIGHT

class Solution:
    def kthSmallest(self,root:Optional(TreeNode),k:int) -> int:
        count = [k]
        ans = [0]
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if count[0] == 1:
                ans[0] = node.val
            count[0] = count[0] - 1
            
            if count[0] > 0:
                dfs(node.right)

        dfs(root)
        return ans[0]