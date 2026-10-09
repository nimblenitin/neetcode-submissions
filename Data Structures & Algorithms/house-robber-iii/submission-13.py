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
            
            leftVal = dfs(node.left)
            rightVal = dfs(node.right)
        
            withRoot = node.val + leftVal[1] + rightVal[1]
            withoutRoot = max(leftVal) + max(rightVal)
            
            return [withRoot, withoutRoot]
        return max(dfs(root))