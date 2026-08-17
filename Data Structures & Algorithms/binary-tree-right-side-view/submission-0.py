# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            level_len = len(queue)
            right_side = 0
            for i in range(level_len):
                curr_node = queue.popleft()
                right_side = curr_node.val
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            res.append(right_side)
        
        return res