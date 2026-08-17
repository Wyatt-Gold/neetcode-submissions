# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.k = k

        def dfs(root):
            stop = False
            if root.left:
                stop = dfs(root.left)

            if not stop:
                if self.k == 1:
                    self.res = root.val
                    return True
                self.k -= 1
                if root.right:
                    stop = dfs(root.right)
            return stop
            
            
        dfs(root)
        return self.res