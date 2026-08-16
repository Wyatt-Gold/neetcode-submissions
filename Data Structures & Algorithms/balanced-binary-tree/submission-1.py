# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def dfs(root):
            if root == None:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(dfs(root.left) - dfs(root.right)) <= 1