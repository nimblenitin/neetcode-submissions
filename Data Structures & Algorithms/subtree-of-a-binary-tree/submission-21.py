# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root and not subRoot:
            return True
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def sameTree(self, treeOne, treeTwo):
        if not treeOne and not treeTwo:
            return True
        if not treeOne or not treeTwo:
            return False
        
        
        if treeOne.val == treeTwo.val:
            return (self.sameTree(treeOne.left, treeTwo.left) and self.sameTree(treeOne.right, treeTwo.right))
        return False