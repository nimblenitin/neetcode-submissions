# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)
            res = max(res, leftmax + rightmax)
            return 1 + max(leftmax, rightmax)

        dfs(root)
        return res