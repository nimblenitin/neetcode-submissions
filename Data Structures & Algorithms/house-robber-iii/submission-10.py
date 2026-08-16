# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            
            leftCal = dfs(node.left)
            rightCal = dfs(node.right)
            withRoot = node.val + leftCal[1] + rightCal[1]
            withoutRoot = max(leftCal) + max(rightCal)
            return [withRoot, withoutRoot]
        return max(dfs(root))

            