# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodeStack = [(root, 1)]
        res = 0
        while nodeStack:
            node, rank = nodeStack.pop()
            if node:
                res = max(res, rank)
                nodeStack.append((node.left, rank + 1))
                nodeStack.append((node.right, rank + 1))
        return res
        
        

            
