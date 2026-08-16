# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        def dfs(root):
            if root == None:
                return 0
            
            l_height = dfs(root.left)
            r_height = dfs(root.right)
            self.max_depth = max(self.max_depth, l_height + r_height)
            return max(l_height, r_height) + 1

        dfs(root)
        return self.max_depth