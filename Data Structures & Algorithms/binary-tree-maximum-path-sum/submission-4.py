# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')

        def dfs(root):
            if not root:
                return 0
            max_left = max(0, dfs(root.left))
            max_right = max(0, dfs(root.right))
            self.max_path_sum = max(self.max_path_sum, max_left + root.val + max_right)

            return max(root.val + max_left, root.val + max_right)

        dfs(root)
        return self.max_path_sum