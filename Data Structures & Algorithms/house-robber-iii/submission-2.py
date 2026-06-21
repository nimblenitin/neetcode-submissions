# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]
            
            rootLeft = dfs(root.left)
            rootRight = dfs(root.right)
            withRoot = root.val + rootLeft[1] + rootRight[1]
            withoutRoot = max(rootLeft) + max(rootRight)
            return [withRoot, withoutRoot]
        return max(dfs(root))  